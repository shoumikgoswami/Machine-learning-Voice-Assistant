# Machine-learning-Voice-Assistant

## Anna - A Voice Command driven Virtual Assistant for running Data Analysis

The idea is to create a voice enabled assistant which can run automated statistical analysis on any given dataset and any model on top of it.

Check the demo video in DEMO folder for a glimpse of how the assistant works on voice commands.

### **Anna v0.1 features -**

1. Support OSEMN data pipeline - <br>
  *O — Obtaining our data <br>
  S — Scrubbing / Cleaning our data <br>
  E — Exploring / Visualizing our data will allow us to find patterns and trends <br>
  M — Modeling our data will give us our predictive power as a wizard <br>
  N — Interpreting our data* <br>
2. Supports uploading a CSV dataset using file browser.
3. Supports data description, data cleaning and data visualisation.
4. Supports pairplot for v0.1.
5. Supports cleaning the dataset for any NAN values on request.
6. Supports 5 clasification models -  <br>
  *Logisitic regression <br>
  K Neighbors Classifier <br>
  Decision Tree Classifier <br>
  Gaussian NB Classifier <br>
  Support Vector Classifier* <br>
7. Supports Train-Test splits and K Fold cross validation.

### **Anna v0.2 features - ** 

1. Supports multiple visualisations.
2. Supports multiple models and evaluation reports.
3. Supports downloading models to disk.
4. Supports numerical datasets of any size.

### **Anna v0.3 features - ** [Current Version]

1. Modular code (function based for easy jump offs)
2. Login and Log off feature
3. Text to intent and action matching (inputs are generalized now, no hard coded commands)
4. Voice and chat support based on user selection
5. User can directly upload data and ask the bot to build a model (does not have to go through the entire pipeline and select a model from the list)
6. Request based data exploration
- Includes head, tail functions based on user specified rows
- Data distribution details
- Display unique values in the columns
- Display columns with NAN values
- Display count of columns per data type

## How to use Anna - 
1. Install necessary dependencies
2. Create a API access token in wit.ai 
3. Update token in speech_to_text.py file
4. Use any dataset from the sample

