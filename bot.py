''' Anna v0.2 - Your personal assitant for building machine learning models.
Creator - @shoumikgoswami
The idea is to create a voice enabled assistant which can run automated statistical analysis on any given dataset and any model on top of it.

Check the demo video in DEMO folder for a glimpse of how the assistant works on voice commands.

Anna v0.1 features -
1. Support OSEMN data pipeline - 
	O — Obtaining our data 
	S — Scrubbing / Cleaning our data 
	E — Exploring / Visualizing our data will allow us to find patterns and trends 
	M — Modeling our data will give us our predictive power as a wizard 
	N — Interpreting our data 
2. Supports uploading a CSV dataset using file browser.
3. Supports data description, data cleaning and data visualisation.
4. Supports pairplot for v0.1.
5. Supports cleaning the dataset for any NAN values on request.
6. Supports 5 clasification models - 
	Logisitic regression 
	K Neighbors Classifier 
	Decision Tree Classifier 
	Gaussian NB Classifier 
	Support Vector Classifier 
7. Supports Train-Test splits and K Fold cross validation.

**Anna v0.2 features - ** [Current version]
1. Support multiple visualisations on request.
2. Support multiple models and reports.
3. Support downloading models to disk. 

How to use Anna - 
1. Install necessary dependencies
2. Create a API access token in wit.ai 
3. Update token in speech_to_text.py file'''


from speech_to_text import RecognizeSpeech
import random
import datetime
import pyttsx3
import speech_recognition as sr
import pandas as pd
from data_analysis import loaddata, describedata, generategraphs, build_model
import sys


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

greetings = ['hey there anna', 'hello anna', 'hi anna', 'Hai anna', 'hey! anna', 'hey anna']
var1 = ['upload a dataset', 'load dataset', 'load data', 'upload data']
var2 = ['what can you do', 'show me your skills','show options', 'help me']
var3 = ['describe the dataset', 'what is in my dataset', 'can you describe the dataset', 'describe the data', 'describe data']
var4 = ['clean the dataset', 'clean dataset', 'clean the data', 'clean my dataset', 'clean the data set']
var5 = ['visualize','generate graphs', 'create graphs', 'visualize the dataset', 'create plots', 'plot the dataset', 'show the dataset', 'build plots']
var6 = ['build models', 'build a classification model', 'create a classification model', 'build model']
LR = ['logistic regression', 'logistic regression model', 'logistic regression classifier', 'regression']
KNN = ['okay neighbors', 'k n n', 'okay neighbors classifier']
CART = ['decision tree', 'decision tree classifier', 'decision trees']
NB = ['gaussian', 'bayes', 'gaussian n b', 'naive bayes']
SVC = ['support vector', 'support vector machine', 'support vector classifier']
var7 = ['bye', 'cya', 'good bye', 'thank you']

repfr9 = ['youre welcome', 'glad i could help you']


try:
	while True:
		text =  RecognizeSpeech('myspeech.wav', 4)
		print("I heard: ", text)
		if text in greetings:
			print("Hello! I am Anna, your personal data analysis assistant. I can help you analyze your data and build machine learning models. What would you like me to do today?")
			engine.say("Hello! I am Anna, your personal data analysis assistant. I can help you analyze your data and build machine learning models. What would you like me to do today?")
			print("Hint - Ask me what I can do")
			engine.runAndWait()
		elif text in var1:
			engine.say("Sure, please provide the link to dataset")
			print("Sure, please provide the link to dataset")
			engine.runAndWait()
			data = loaddata()
			print("Dataset loaded. Here are the top 5 rows")
			engine.say("Dataset loaded. Here are the top 5 rows")
			print("Dataset: ", data.head())
			engine.runAndWait()
		elif text in var2:
			engine.say("I can do a number of actions, please follow the below steps for data analysis")
			print("I can do a number of actions, please follow the below steps for data analysis")
			print("1. Upload a dataset")
			print("2. Describe the dataset")
			print("3. Clean the dataset")
			print("4. Generate basic graphs")
			print("5. Build classification model")
			print("6. Generate model performance scores")
			print("7. Test the model")
			engine.runAndWait()
		elif text in var3:
			engine.say("Let me show you how the dataset looks")
			print("Let me show you how the dataset looks")
			describedata(data)
			if data.isnull().values.any() == True:
				engine.say("Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
				print("Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
			else:
				engine.say("Dataset has no NaN values. You are good to go.")
				print("Dataset has no NaN values. You are good to go.")
				clean_data = data
			engine.runAndWait()
		elif text in var4:
			if data.isnull().values.any() == True:
				engine.say("Hold on let me clean the dataset for you.")
				print("Hold on let me clean the dataset for you.")
				clean_data = data.dropna(how = 'any')
				engine.say("Let me describe the clean dataset for you.")
				print("Let me describe the clean dataset for you.")
				describedata(clean_data)
			else:
				engine.say("Dataset is already clean.")
				print("Dataset is already clean.")
			engine.runAndWait()
		elif text in var5:
			engine.say("Hold on, let me create some visualizations for you.")
			print("Hold on let me create some visualizations for you.")
			engine.runAndWait()
			generategraphs(clean_data)
		elif text in var6:
			engine.say("Before I build a model for you, please choose the label column.")
			print("Before I build a model for you, please choose the label column.")
			engine.runAndWait()
			print(clean_data.columns.values)
			col_names = list(clean_data.columns.values)
			col = RecognizeSpeech('myspeech.wav', 4)
			if col in col_names:
				Y = clean_data[col]
				engine.say("Label column set")
				print("Label column set")
				engine.runAndWait()
			else:
				engine.say("Rebuild the model")
				print("Rebuild the model")
				engine.runAndWait()
			X = clean_data.drop(col, axis = 1)
			engine.say("Below are the first 5 features.")
			print("Below are the first 5 features: ", X.head())
			engine.runAndWait()
			engine.say("Below are the first 5 labels.")
			print("Below are the first 5 labels: ", Y.head())
			engine.runAndWait()
			engine.say("Choose one model from the list.")
			print("Choose one model from the list:")
			engine.runAndWait()
			print("1. Logistic Regression")
			print("2. K Neighbors Classifier")
			print("3. Decision Tree Classifier")
			print("4. Gaussian NB")
			print("5. Support Vector Classifier")
			model_name = RecognizeSpeech('myspeech.wav', 4)
			if model_name in LR:
				engine.say("Hold on let me build the model for you.")
				print("Hold on let me build the model for you.")
				engine.runAndWait()
				build_model('Logistic Regression model', X, Y)
				engine.say("Done! I have also saved a copy of the model for you.")
				print("Done! I have also saved a copy of the model for you.")
				engine.runAndWait()
			elif model_name in KNN:
				engine.say("Hold on let me build the model for you.")
				print("Hold on let me build the model for you.")
				engine.runAndWait()
				build_model('K Neighbors Classifier', X, Y)
				engine.say("Done! I have also saved a copy of the model for you.")
				print("Done! I have also saved a copy of the model for you.")
				engine.runAndWait()
			elif model_name in CART:
				engine.say("Hold on let me build the model for you.")
				print("Hold on let me build the model for you.")
				engine.runAndWait()
				build_model('Decision Tree Classifier', X, Y)
				engine.say("Done! I have also saved a copy of the model for you.")
				print("Done! I have also saved a copy of the model for you.")
				engine.runAndWait()
			elif model_name in NB:
				engine.say("Hold on let me build the model for you.")
				print("Hold on let me build the model for you.")
				engine.runAndWait()
				build_model('Gaussian NB', X, Y)
				engine.say("Done! I have also saved a copy of the model for you.")
				print("Done! I have also saved a copy of the model for you.")
				engine.runAndWait()
			elif model_name in SVC:
				engine.say("Hold on let me build the model for you.")
				print("Hold on let me build the model for you.")
				engine.runAndWait()	
				build_model('Support Vector Classifier', X, Y)
				engine.say("Done! I have also saved a copy of the model for you.")
				print("Done! I have also saved a copy of the model for you.")
				engine.runAndWait()
			else:
				engine.say("Please choose a model")
				engine.runAndWait()
				print("Please choose a model")
		elif text in var7:
			engine.say("Thank you for using me.")
			print("Thank you for using me.")
			engine.runAndWait()
			sys.exit()
			
except Exception as e: print(e)
	#engine.say("Exception triggered")
	#print("Exception triggered")
	#Exception as e: print(e)
		
	