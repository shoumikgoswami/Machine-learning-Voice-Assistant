''' Anna v0.3 - Your personal assitant for building machine learning models.
Creator - @shoumikgoswami
The idea is to create a voice enabled assistant which can run automated statistical analysis on any given dataset and any model on top of it.

Check the demo video in DEMO folder for a glimpse of how the assistant works on voice commands.

Version 0.3 changelog - 
1. Modular codes to allow jump offs
2. Login-Log off feature
3. Voice and Chat support
4. Intent to action matching

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
import time
from intent_finder import get_intent

# ********************** Setting voice parameters **********************
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# ********************** Functions **********************

def get_mode():
	engine.say("Do you want to chat with me or speak to me?")
	print("Do you want to chat with me or speak to me?")
	engine.runAndWait()
	mode_text =  input("Enter mode: ")
	if mode_text in ('chat','text'):
		print("Text mode set")
		return 'TEXT'
	elif mode_text in ('speak', 'voice'):
		engine.say("Voice mode set")
		print("Voice mode set")
		engine.runAndWait()
		return 'VOICE'
	else:
		get_mode()

def askUser(mode):
	if mode =='TEXT':
		username = input("Enter your Name: ")
		password = input("Enter your access code: ")
		if password == "password":
			return username
		else:
			print("Your access code was incorrect")
			askUser('TEXT')
	elif mode == 'VOICE':
		engine.say("May i know your name?")
		print("May i know your name?")
		engine.runAndWait()
		username = RecognizeSpeech('myspeech.wav', 4)
		print("I heard: ", username)
		engine.say("Please tell me your access code")
		print("Please tell me your access code")
		engine.runAndWait()
		password = RecognizeSpeech('myspeech.wav', 4)
		if password == "password":
			return username
		else:
			engine.say("Your access code was incorrect")
			print("Your access code was incorrect")
			engine.runAndWait()
			get_mode()

def welcome_user(mode):
	if mode == 'TEXT':
		print("Welcome " + username)
		print("You have successfully logged in!")
	elif mode == 'VOICE':
		engine.say("Welcome"+ username)
		print("Welcome " + username)
		engine.runAndWait()
		engine.say("You have successfully logged in!")
		print("You have successfully logged in!")
		engine.runAndWait()
	else:
		mode = get_mode()

def get_text(mode):
	if mode == 'TEXT':
		text = input("Enter your command: ")
		return text
	elif mode == 'VOICE':
		text =  RecognizeSpeech('myspeech.wav', 4)
		print("I heard: ", text)
		return text
	else: 
		get_mode()

def cmd_upload_data(mode):
	if mode == 'TEXT':
		print("Please provide the link to dataset")
		data = loaddata()
		print("Dataset loaded. Here are the top 5 rows")
		print("Dataset: ", data.head())
		return data
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
		engine.say("Please provide the link to dataset")
		print("Please provide the link to dataset")
		engine.runAndWait()
		data = loaddata()
		print("Dataset loaded. Here are the top 5 rows")
		engine.say("Dataset loaded. Here are the top 5 rows")
		print("Dataset: ", data.head())
		engine.runAndWait()
		return data
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()

def cmd_describe_data(mode, data):
	if mode == 'TEXT':
		print("Let me show you how the dataset looks")
		describedata(data)
		if data.isnull().values.any() == True:
			print("Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
			return data
		else:
			print("Dataset has no NaN values. You are good to go.")
			clean_data = data
			return clean_data
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
		engine.say("Let me show you how the dataset looks")
		print("Let me show you how the dataset looks")
		describedata(data)
		if data.isnull().values.any() == True:
			engine.say("Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
			print("Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
			return data
		else:
			engine.say("Dataset has no NaN values. You are good to go.")
			print("Dataset has no NaN values. You are good to go.")
			clean_data = data
			return clean_data
		engine.runAndWait()
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()
		
def cmd_clean_data(mode, data):
	if mode == 'TEXT':
		if data.isnull().values.any() == True:
			print("Hold on let me clean the dataset for you.")
			clean_data = data.dropna(how = 'any')
			print("Let me describe the clean dataset for you.")
			describedata(clean_data)
			return clean_data
		else:
			print("Dataset is already clean.")
			return data
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
		if data.isnull().values.any() == True:
			engine.say("Hold on let me clean the dataset for you.")
			print("Hold on let me clean the dataset for you.")
			clean_data = data.dropna(how = 'any')
			engine.say("Let me describe the clean dataset for you.")
			print("Let me describe the clean dataset for you.")
			describedata(clean_data)
			return clean_data
		else:
			engine.say("Dataset is already clean.")
			print("Dataset is already clean.")
			return data
		engine.runAndWait()
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()
	
def cmd_features(mode):
	if mode == 'TEXT':
		print("I can do a number of actions, please follow the below steps for data analysis")
		print("1. Upload a dataset")
		print("2. Describe the dataset")
		print("3. Clean the dataset")
		print("4. Generate basic graphs")
		print("5. Build classification model")
		print("6. Generate model performance scores")
		print("7. Test the model")
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
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
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()

def cmd_visualize(mode, data):
	if mode == 'TEXT':
		print("Hold on let me create some visualizations for you.")
		generategraphs(data)
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
		engine.say("Hold on, let me create some visualizations for you.")
		print("Hold on let me create some visualizations for you.")
		engine.runAndWait()
		generategraphs(data)
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()

def cmd_build_model(mode, model_type, data):
	if mode == 'TEXT':
		print("Before I build a model for you, please choose the label column.")
		print(data.columns.values)
		col_names = list(data.columns.values)
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			print("Label column set")
		else:
			print("Rebuild the model")
			cmd_build_model(mode, model_type, data)
		X = data.drop(col, axis = 1)
		print("Below are the first 5 features: ", X.head())
		print("Below are the first 5 labels: ", Y.head())
		if model_type != 0:
			model_builder(mode, model_type, X, Y)
		else:
			print("Choose one model from the list:")
			print("1. Logistic Regression")
			print("2. K Neighbors Classifier")
			print("3. Decision Tree Classifier")
			print("4. Gaussian NB")
			print("5. Support Vector Classifier")
			text =  get_text(mode)
			cmd, model_type = get_intent(text)
			model_builder(mode, model_type, X, Y)
		text =  get_text(mode)
		cmd = get_intent(text)
	elif mode == 'VOICE':
		engine.say("Before I build a model for you, please choose the label column.")
		print("Before I build a model for you, please choose the label column.")
		engine.runAndWait()
		print(data.columns.values)
		col_names = list(data.columns.values)
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			engine.say("Label column set")
			print("Label column set")
			engine.runAndWait()
		else:
			engine.say("Rebuild the model")
			print("Rebuild the model")
			engine.runAndWait()
			cmd_build_model(mode, model_type, data)
		X = data.drop(col, axis = 1)
		engine.say("Below are the first 5 features.")
		print("Below are the first 5 features: ", X.head())
		engine.runAndWait()
		engine.say("Below are the first 5 labels.")
		print("Below are the first 5 labels: ", Y.head())
		engine.runAndWait()
		if model_type != 0:
			model_builder(mode, model_type, X, Y)
		else:
			engine.say("Choose one model from the list.")
			print("Choose one model from the list:")
			engine.runAndWait()
			print("1. Logistic Regression")
			print("2. K Neighbors Classifier")
			print("3. Decision Tree Classifier")
			print("4. Gaussian NB")
			print("5. Support Vector Classifier")
			text =  get_text(mode)
			cmd, model_type = get_intent(text)
			model_builder(mode, model_type, X, Y)
		text =  get_text(mode)
		cmd = get_intent(text)
	else:
		get_mode()

def model_builder(mode, model_name, X, Y):
	if mode == 'TEXT':
		if model_name == 'LR':
			print("Hold on let me build the model for you.")
			build_model('Logistic Regression model', X, Y)
			print("Done! I have also saved a copy of the model for you.")
		elif model_name == 'KNN':
			print("Hold on let me build the model for you.")
			build_model('K Neighbors Classifier', X, Y)
			print("Done! I have also saved a copy of the model for you.")
		elif model_name == 'CART':
			print("Hold on let me build the model for you.")
			build_model('Decision Tree Classifier', X, Y)
			print("Done! I have also saved a copy of the model for you.")
		elif model_name == 'NB':
			print("Hold on let me build the model for you.")
			build_model('Gaussian NB', X, Y)
			print("Done! I have also saved a copy of the model for you.")
		elif model_name == 'SVC':
			print("Hold on let me build the model for you.")	
			build_model('Support Vector Classifier', X, Y)
			print("Done! I have also saved a copy of the model for you.")
		else:
			cmd_build_model(mode, model_type, data)
	elif mode == 'VOICE':
		if model_name == 'LR':
			engine.say("Hold on let me build the model for you.")
			print("Hold on let me build the model for you.")
			engine.runAndWait()
			build_model('Logistic Regression model', X, Y)
			engine.say("Done! I have also saved a copy of the model for you.")
			print("Done! I have also saved a copy of the model for you.")
			engine.runAndWait()
		elif model_name == 'KNN':
			engine.say("Hold on let me build the model for you.")
			print("Hold on let me build the model for you.")
			engine.runAndWait()
			build_model('K Neighbors Classifier', X, Y)
			engine.say("Done! I have also saved a copy of the model for you.")
			print("Done! I have also saved a copy of the model for you.")
			engine.runAndWait()
		elif model_name == 'CART':
			engine.say("Hold on let me build the model for you.")
			print("Hold on let me build the model for you.")
			engine.runAndWait()
			build_model('Decision Tree Classifier', X, Y)
			engine.say("Done! I have also saved a copy of the model for you.")
			print("Done! I have also saved a copy of the model for you.")
			engine.runAndWait()
		elif model_name == 'NB':
			engine.say("Hold on let me build the model for you.")
			print("Hold on let me build the model for you.")
			engine.runAndWait()
			build_model('Gaussian NB', X, Y)
			engine.say("Done! I have also saved a copy of the model for you.")
			print("Done! I have also saved a copy of the model for you.")
			engine.runAndWait()
		elif model_name == 'SVC':
			engine.say("Hold on let me build the model for you.")
			print("Hold on let me build the model for you.")
			engine.runAndWait()	
			build_model('Support Vector Classifier', X, Y)
			engine.say("Done! I have also saved a copy of the model for you.")
			print("Done! I have also saved a copy of the model for you.")
			engine.runAndWait()
		else:
			cmd_build_model(mode, model_type, data)
	else:
		get_mode()

# ********************** Initiate Anna **********************

print("************* Initiating Anna *************")
engine.say("Initiating Anna")
engine.runAndWait()
time.sleep(2)
engine.say("Hello! I am Anna, your personal data analysis assistant. I can help you analyze your data and build machine learning models.")
print("Hello! I am Anna, your personal data analysis assistant. I can help you analyze your data and build machine learning models.")
engine.runAndWait()
 
mode = get_mode()
username = askUser(mode)
welcome_user(mode)

try:
	while True:
		text =  get_text(mode)
		cmd, model_type = get_intent(text)
		if cmd == '1U':
			data = cmd_upload_data(mode)
		elif cmd == '4F':
			cmd_features(mode)
		elif cmd == '2D':
			cmd_describe_data(mode, data)
		elif cmd == '3C':
			data = cmd_clean_data(mode, data)		
		elif cmd == '5V':
			cmd_visualize(mode, data)
		elif cmd == '6B':
			cmd_build_model(mode, model_type, data)
		elif cmd == 'bye':
			engine.say("Thank you for using me.")
			print("Thank you for using me.")
			engine.runAndWait()
			sys.exit()
		else:
			get_mode()
			
except Exception as e: print(e)
	#engine.say("Exception triggered")
	#print("Exception triggered")
	#Exception as e: print(e)
		
	