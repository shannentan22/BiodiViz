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

If you wish to run the application, you must follow the proceeding steps:

### 1. Cloning this Github repository

In downloading repositories from Github, there are multiple methods, all of which can be searched online. For this user manual, we shall explain the two methods that we believe are the simplest. Note that our instructions and descriptions are based on the current interface of Github as of June 14, 2024.

#### Method 1: Download as ZIP file

1. Access the [BiodiViz Github repository](https://github.com/shannentan22/BiodiViz/).
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

Since the Named Entity Recognition (NER) and Relation Extraction (RE) Models are too big to be included in the Github repository, you may download them from the pre-release attachments instead: [https://github.com/shannentan22/BiodiViz/releases/tag/v1.0.0](https://github.com/shannentan22/BiodiViz/releases/tag/v1.0.0).
The files are named `ner_model.zip` and `re_model.zip`.

Before downloading, please ensure that you have enough space to accommodate the models since each file is fairly large at about 760+ MB. The download process may also take a few minutes due to the files' sizes. After downloading the files, unzip them, and move the unzipped folders under the App folder of the cloned repository. 

## References

[1] Abdelmageed, N., Löffler, F., Feddoul, L., Algergawy, A., Samuel, S., Gaikwad, J., ... & König-Ries, B. (2022). BiodivNERE: Gold standard corpora for named entity recognition and relation extraction in the biodiversity domain. Biodiversity Data Journal, 10.
