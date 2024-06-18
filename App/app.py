from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from itertools import combinations
from werkzeug.utils import secure_filename
import docx
import PyPDF2
import os
import shutil
import torch
import nltk
nltk.download('punkt')

# File upload set-up
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'docx', 'pdf'}

# Initialize the data dictionary
data = {
    "nodes": [],
    "links": []
}

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# FUNCTIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ''
    
    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    elif ext == '.doc' or ext == '.docx':
        doc = docx.Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    elif ext == '.pdf':
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = '\n'.join([reader.pages[i].extract_text() for i in range(len(reader.pages))])
    
    return text

def delete_uploads_folder():
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])
    os.makedirs(app.config['UPLOAD_FOLDER'])

# ROUTES

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def upload():
    global data
    delete_uploads_folder()
    if request.method == 'POST':
        button_type = request.form.get('button_type')
        if 'file' in request.files or button_type == 'initial':
            if 'file' in request.files:
                file = request.files['file']
                if file and file.filename != '':
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    
                    # Identify the file type
                    file_ext = os.path.splitext(file.filename)[1].lower()

                    if allowed_file(file_ext):
                        paragraph = extract_text_from_file(file_path)
            elif button_type == 'initial':
                paragraph = request.form.get('input')
            
            # Clear the data dictionary
            data = {
                "nodes": [],
                "links": []
            }

            # Load the model using Hugging Face pipeline
            device = 1 if torch.cuda.is_available() else -1

            ner = "./ner_model"
            token_classifier = pipeline("token-classification", model=ner, aggregation_strategy="first", device=device)
            re = "./re_model"
            re_classifier = pipeline("sentiment-analysis", model=re, device=device)

            sentences = nltk.sent_tokenize(paragraph)
            for s in sentences:
                print(s)
            
            # Iterate through each sentence in the paragraph
            for s in sentences:
                entity_list = token_classifier(s)
                res = entity_list

                def mask_entities(sentence, entities, mask_entities):
                    masked_sentence = sentence
                    offset = 0  # Offset for adjusting indices
                    masked_words = []  # Store the masked words
                    for entity in entities:
                        if entity in mask_entities:
                            entity_group = entity['entity_group'].upper() 
                            masked_word = f"@{entity_group}$"
                            masked_words.append(entity['word'])
                        else: 
                            masked_word = entity['word']
                        start = entity['start'] + offset
                        end = entity['end'] + offset
                        masked_sentence = masked_sentence[:start] + masked_word + masked_sentence[end:]
                        offset += len(masked_word) - len(entity['word'])  # Adjust offset for next replacement
                    return masked_sentence, masked_words

                # Generate combinations of 2 entities to mask
                combinations_to_mask = list(combinations(res, 2))

                # List to store masked sentences and masked words for each combination
                masked_sentences = []

                # Create masked sentences and masked words for each combination
                for combo in combinations_to_mask:
                    # Mask the entities in the original sentence for this combination
                    masked_sentence, masked_words = mask_entities(s, res, combo)
                    masked_sentences.append((masked_sentence, masked_words, [combo[0]['entity_group'], combo[1]['entity_group']]))

                related_words = []
                categories = []
                relations = []
                label_mapping = {
                    'LABEL_1': 'have',
                    'LABEL_2': 'occur_in',
                    'LABEL_3': 'influence'
                }
                for masked in masked_sentences:
                    results = re_classifier(masked[0])
                    if results[0]['label'] != 'LABEL_0':
                        related_words.append(masked[1])
                        categories.append(masked[2])
                        relations.append(label_mapping.get(results[0]['label']))

                for i in range(len(related_words)):
                    node1 = {"name": related_words[i][0], "category": categories[i][0]}
                    node2 = {"name": related_words[i][1], "category": categories[i][1]}
                    link = {"source": related_words[i][0], "target": related_words[i][1], "relation": relations[i], "value": 2}
                    if node1 not in data['nodes']:
                        data['nodes'].append(node1)
                    if node2 not in data['nodes']:
                        data['nodes'].append(node2)
                    if link not in data['links']:
                        data['links'].append(link)

                categories_string = "Organism, Environment, Quality, Location, Phenomena, Matter"
                relations_string = "have, occur_in, influence, none"
            return render_template('/graph.html', data=data, categories=categories_string, relations=relations_string)
        
        elif button_type == 'filter':
            categories = [request.form.get('Organism'), 
                          request.form.get('Environment'), 
                          request.form.get('Quality'),
                          request.form.get('Location'),
                          request.form.get('Phenomena'),
                          request.form.get('Matter')]
            relations = [request.form.get('have'),
                         request.form.get('occur_in'),
                         request.form.get('influence'),
                         request.form.get('none')]

            filtered_nodes = [node for node in data['nodes'] if node['category'] in categories]
            # Create a set of node names from the filtered nodes
            filtered_node_names = {node['name'] for node in filtered_nodes}
            # Filter links that have source and target in the set of filtered node names
            filtered_links = [link for link in data['links'] if link['relation'] in relations and link['source'] in filtered_node_names and link['target'] in filtered_node_names]
            # If "none" is in the selected relations, include all nodes. Otherwise, only include nodes that have a name in the set of filtered node names.
            if 'none' in relations:
                pass
            else:
                # Create a set of node names that appear in the source or target of any link
                linked_node_names = {link['source'] for link in filtered_links}.union({link['target'] for link in filtered_links})
                # Filter nodes that have a name in the set of linked node names
                filtered_nodes = [node for node in filtered_nodes if node['name'] in linked_node_names]
            filtered_graph_data = {'nodes': filtered_nodes, 'links': filtered_links}
            
            # Filter out any None values from the categories list
            selected_categories = [category for category in categories if category is not None]
            # Concatenate the selected categories into a single string
            categories_string = ', '.join(selected_categories)

            # Filter out any None values from the relations list
            selected_relations = [relation for relation in relations if relation is not None]
            # Concatenate the selected relations into a single string
            relations_string = ', '.join(selected_relations)

            return render_template('/graph.html', data=filtered_graph_data, categories=categories_string, relations=relations_string)
    else:
        return 'Only POST requests are allowed'


if __name__ == '__main__':
    app.run()