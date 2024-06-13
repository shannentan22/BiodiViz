# BiodiViz

This repository contains the codes and outputs of **Angela Shannen Tan**'s and **Paul Michael Dimayuga**'s undergraduate thesis at the *Computer Vision and Machine Intelligence Group, Department of Computer Science, University of the Philippines Diliman*. Our research involves applying Natural Language Processing (NLP) techniques to contribute to the digitalization of the field of biodiversity. There three main components to our work: 
- Named Entity Recognition (NER) training,
- Relation Extraction (RE) training, and
- a BiodiViz knowledge graph application that integrates the previous two components.

This README contains an explanation on the contents of the repository and how to navigate it.

## Datasets

Two datasets were used for this research, both of which were taken from the [BiodivNERE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9836593/) corpora by Abdelmageed et al. (2022) [1]. Our NER training utilized the **BiodivNER** dataset, while the RE training utilized **BiodivRE** MultiClass.

A copy of these corpora is also in our repository, under the *Datasets* folder. Each dataset contains three CSV files for the development/validation, train, and test sets, each of which serve a different purpose in the training process.

## References

[1] Abdelmageed, N., Löffler, F., Feddoul, L., Algergawy, A., Samuel, S., Gaikwad, J., ... & König-Ries, B. (2022). BiodivNERE: Gold standard corpora for named entity recognition and relation extraction in the biodiversity domain. Biodiversity Data Journal, 10.
