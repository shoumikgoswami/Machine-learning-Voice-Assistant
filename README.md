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

### **Anna v0.2 features - ** [Current Version]

1. Supports multiple visualisations.
2. Supports multiple models and evaluation reports.
3. Supports downloading models to disk.
4. Supports numerical datasets of any size.

## How to use Anna - 
1. Install necessary dependencies
2. Create a API access token in wit.ai 
3. Update token in speech_to_text.py file
4. Use any dataset from the sample

## Voice commands supported - 

greetings = ['hey there anna', 'hello anna', 'hi anna', 'Hai anna', 'hey! anna', 'hey anna'] <br>
var1 = ['upload a dataset', 'load dataset', 'load data', 'upload data'] <br>
var2 = ['what can you do', 'show me your skills','show options', 'help me'] <br>
var3 = ['describe the dataset', 'what is in my dataset', 'can you describe the dataset', 'describe the data', 'describe data'] <br>
var4 = ['clean the dataset', 'clean dataset', 'clean the data', 'clean my dataset', 'clean the data set'] <br>
var5 = ['visualize','generate graphs', 'create graphs', 'visualize the dataset', 'create plots', 'plot the dataset', 'show the dataset', 'build plots'] <br>
var6 = ['build models', 'build a classification model', 'create a classification model', 'build model'] <br>
LR = ['logistic regression', 'logistic regression model', 'logistic regression classifier', 'regression'] <br>
KNN = ['okay neighbors', 'k n n', 'okay neighbors classifier'] <br>
CART = ['decision tree', 'decision tree classifier', 'decision trees'] <br>
NB = ['gaussian', 'bayes', 'gaussian n b', 'naive bayes'] <br>
SVC = ['support vector', 'support vector machine', 'support vector classifier'] <br>
var7 = ['bye', 'cya', 'good bye', 'thank you'] <br>
