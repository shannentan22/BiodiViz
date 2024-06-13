# BiodiViz

This repository contains the codes and outputs of **Angela Shannen Tan**'s and **Paul Michael Dimayuga**'s undergraduate thesis at the *Computer Vision and Machine Intelligence Group, Department of Computer Science, University of the Philippines Diliman*. Our research involves applying Natural Language Processing (NLP) techniques to contribute to the digitalization of the field of biodiversity. There three main components to our work: 
- Named Entity Recognition (NER) training,
- Relation Extraction (RE) training, and
- a BiodiViz knowledge graph application that integrates the previous two components.

This README contains an explanation on the contents of the repository and how to navigate it.

## Datasets

Two datasets were used for this research, both of which were taken from the [BiodivNERE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9836593/) corpora by Abdelmageed et al. (2022) [1]. Our NER training utilized the **BiodivNER** dataset, while the RE training utilized **BiodivRE** MultiClass.

A copy of these corpora is also in our repository, under the *Datasets* folder. Each dataset contains three CSV files for the development/validation, train, and test sets, each of which serve a different purpose in the training process.

## NER and RE Finetuning

The source codes for the NER and RE training can be found under the *Finetuning* folder. In each notebook, there are sections for package installation, data preprocessing, model fine-tuning, model inference, and model evaluation. For the RE notebooks, there is an additional hyperparameter optimization section.

To run the Jupyter Notebooks yourself:
1. Clone or download the repository to your system.
2. Ensure that you have Python 3.12.1 installed in your system.
3. Optionally, you may create a virtual environment before installing the packages.
4. Select the file of the model you want to run and open it in your chosen text editor or integrated development environment (IDE).
5. To install the necessary packages, simply uncomment the second block containing the `!pip install ...` lines. You only need to do this once for NER and once for RE, per environment.
6. Then, you may run all of the code blocks. The hyperparameter optimization and training may take a few minutes to a couple of hours depending on your GPU size.

## The BiodiViz Application

The *App* folder contains the files for running the BiodiViz application. The files for the web application are under the *static* and *templates* folders. The former folder contains the CSS code and images used for the application, while the latter contains the HTML files. The file for the Python Flask server is *app.py*.

If you wish to run the application, you must follow the proceeding steps. Note that the instructions are tailored to a Windows 10 operating system. Other operating systems should follow a similar process but may be slightly different.

### 1. Cloning this GitHub repository

In downloading repositories from GitHub, there are multiple methods, all of which can be searched online. For this user manual, we shall explain the two methods that we believe are the simplest. Note that our instructions and descriptions are based on the current interface of GitHub as of June 14, 2024.

#### Method 1: Download as ZIP file

1. Access the [BiodiViz GitHub repository](https://github.com/shannentan22/BiodiViz/).
2. Click on the `<>Code` button located above the repository files on the top-right.
3. Click on the `Download ZIP` button at the bottom of the dropdown.
4. Once downloaded, unzip the file.
5. Optionally, you may move the file to a different folder if you wish.

#### Method 2: Clone using the web URL

1. Open Git Bash or Command Prompt on your computer.
2. Optionally, you may change the current working directory to a different location where you want the cloned directory.
3. Type `git clone https://github.com/shannentan22/BiodiViz.git`.
4. Press `Enter` to clone the repository locally.

You may delete the Finetuning and Datasets folders from the repository since they are not needed in the application.

### 2. Downloading the NER & RE Models

Since the Named Entity Recognition (NER) and Relation Extraction (RE) Models are too big to be included in the GitHub repository, you may download them from the pre-release attachments instead: https://github.com/shannentan22/BiodiViz/releases/tag/v1.0.0.
The files are named `ner_model.zip` and `re_model.zip`.

Before downloading, please ensure that you have enough space to accommodate the models since each file is fairly large at about 760+ MB. The download process may also take a few minutes due to the files' sizes. After downloading the files, unzip them, and move the unzipped folders under the App folder of the cloned repository. 

### 3. Installing the Requirements

The following set of instructions need only be performed once for the installation of requirements:

1. Install Python 3.12.1 by downloading the appropriate version from this link: https://www.python.org/downloads/release/python-3121/.
2. Open Command Prompt.
3. Change directory to the App folder of the BiodiViz repository.
4. Create a virtual environment: Enter \texttt{python -m venv venv} in Command Prompt.
5. Activate the virtual environment: Enter `venv\textbackslash Scripts\textbackslash activate.bat` in Command Prompt.
6. Ensure that PIP is installed. If not, visit the PIP website for installation instructions https://pip.pypa.io/en/stable/installation/.
7. Install the packages. Enter `pip install -r requirements.txt` in Command Prompt. This may take a few minutes.
8. You now have all the requirements needed for running the server and application.

### 4. Running the Server

Every time you wish to run the application, the following set of steps must be done:

1. Open Command Prompt
2. Change directory to the App folder of the BiodiViz repository.
3. Activate the virtual environment: Enter `venv\textbackslash Scripts\textbackslash activate.bat` in Command Prompt.
4. Run the server: Enter `flask run --port=8080` in Command Prompt.
5. Enter the link http://127.0.0.1:8080/ into any browser's address bar. You now have access to the BiodiViz application.

### 5. Using the Application

#### a. Main Page

Once you have access to the main page of BiodiViz in your browser, you may input any biodiversity-related text into the text box. Note that longer inputs may also take longer to process. Click `Submit` to generate the knowledge graph.

*Figure 1: BiodiViz main page with sample input text from part of a biodiversity article by Posa et al. [2]*
![Figure 1: BiodiViz main page with sample input text from part of a biodiversity article by Posa et al.](/README_files/userint1.png)

#### b. Knowledge Graph

Once completed, you will be redirected to the graph page displaying the knowledge graph.

*Figure 2: BiodiViz graph page with knowledge graph generated from input text*
![Figure 2: BiodiViz graph page with knowledge graph generated from input text](/README_files/userint2.png)

#### c. Filtering Options

At the top of the graph page, there are filtering options. Choose specific entity categories and relation types you would want to be included in the graph. After clicking `Apply filter`, the intersection of the entity categories and relation types will be displayed in a new knowledge graph.

*Figure 3: BiodiViz filter selection interface*
![Figure 3: BiodiViz filter selection interface](/README_files/userint3.png)

*Figure 4: BiodiViz graph page with filtered knowledge graph*
![Figure 4: BiodiViz graph page with filtered knowledge graph](/README_files/userint4.png)

#### d. Graph Navigation

You can also zoom or pan the graph to navigate it better:
- Scroll up to zoom in.
- Scroll down to zoom out.
- Drag the graph to pan.

#### e. Repeat
To run the application for other input texts, simply go back to the main page and repeat the instructions from this section.

## References

[1] Abdelmageed, N., Löffler, F., Feddoul, L., Algergawy, A., Samuel, S., Gaikwad, J., ... & König-Ries, B. (2022). BiodivNERE: Gold standard corpora for named entity recognition and relation extraction in the biodiversity domain. Biodiversity Data Journal, 10.

[2] Posa, M. R. C., Diesmos, A. C., Sodhi, N. S., & Brooks, T. M. (2008). Hope for threatened tropical biodiversity: lessons from the Philippines. BioScience, 58(3), 231-240.
