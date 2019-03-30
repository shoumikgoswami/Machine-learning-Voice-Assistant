''' Anna v0.5 - Your personal assitant for building machine learning models.
Creator - @shoumikgoswami
The idea is to create a voice enabled assistant which can run automated statistical analysis on any given dataset and any model on top of it.

Check the demo video in DEMO folder for a glimpse of how the assistant works on voice commands.

Version 0.5 changelog - 
1. Removed Wit text classification integration
2. RASA NLU integration implemented

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
from data_analysis import loaddata, describedata, distributionplot, pairplot, build_model, scatterplot, lineplot, histogram, overlaid_histogram, barplot, stackedbarplot
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
		return get_mode()

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
		gen_output(mode, 'May i know your name?')
		username = RecognizeSpeech('myspeech.wav', 4)
		print("I heard: ", username)
		gen_output(mode, 'Please tell me your access code')
		password = RecognizeSpeech('myspeech.wav', 4)
		if password == "password":
			return username
		else:
			gen_output(mode, 'Your access code was incorrect')
			return get_mode()

def welcome_user(mode):
	gen_output(mode, 'Welcome ' + username )
	gen_output(mode, 'You have successfully logged in')

def get_text(mode):
	if mode == 'TEXT':
		text = input("Enter your command: ")
		return text.lower()
	elif mode == 'VOICE':
		text =  RecognizeSpeech('myspeech.wav', 4)
		print("I heard: ", text)
		return text.lower()
	else: 
		return get_mode()

def gen_output(mode, text):
	if mode == 'TEXT':
		print(text)
	elif mode == 'VOICE':
		engine.say(text)
		print(text)
		engine.runAndWait()
	else:
		print('Error, Set mode of interaction')
		return get_mode()

def get_cmd(mode):
	text =  get_text(mode)
	try:
		cmd, cmd_2 = get_intent(text)
		if cmd != 'error':
			return cmd, cmd_2
		else:
			gen_output(mode,"Unable to recognize command, shifting to root menu. Please share your intent again")
			return get_cmd(mode)	
	except:
		gen_output(mode,"Unable to recognize command, shifting to root menu. Please share your intent again")
		with open("log.txt", 'a+') as textfile:
			textfile.write('\n' + text + '\t' + '|' + '\t' + 'error')
		return get_cmd(mode)
	
def cmd_upload_data(mode):
	gen_output(mode,"Please provide the link to dataset")
	data = loaddata()
	gen_output(mode,"Dataset loaded. Here are the top 5 rows")
	print("Dataset: ", data.head())
	return data
	return get_cmd(mode)
	
def cmd_describe_data(mode, data):
	gen_output(mode,"Let me show you how the dataset looks")
	describedata(data)
	if data.isnull().values.any() == True:
		gen_output(mode,"Dataset has NaN values. If you want to remove them, I can clean the dataset for you.")
		return data
	else:
		gen_output(mode,"Dataset has no NaN values. You are good to go.")
		clean_data = data
		return clean_data
	return get_cmd(mode)
		
def cmd_clean_data(mode, data):
	if data.isnull().values.any() == True:
		gen_output(mode,"Hold on let me clean the dataset for you.")
		clean_data = data.dropna(how = 'any')
		gen_output(mode,"Let me describe the clean dataset for you.")
		describedata(clean_data)
		return clean_data
	else:
		gen_output(mode,"Dataset is already clean.")
		return data
	return get_cmd(mode)
	
def cmd_features(mode):
	gen_output(mode,"I can do a number of actions, please follow the below steps for data analysis")
	print("1. Upload a dataset")
	print("2. Describe the dataset")
	print("3. Clean the dataset")
	print("4. Generate basic graphs")
	print("5. Build classification model")
	print("6. Generate model performance scores")
	print("7. Test the model")
	return get_cmd(mode)
	
# To do here
def cmd_visualize(mode, plot_type, data):
	if plot_type != 0:
		plot_builder(mode, plot_type, data)
	else:
		gen_output(mode, "Please select the type of graph from the list.")
		print(" 1. Distribution plot")
		print(" 2. Pair plot")
		print(" 3. Scatter plot")
		print(" 4. Line plot")
		print(" 5. Histogram")
		print(" 6. Overlaid histogram")
		print(" 7. Bar plot")
		print(" 8. Stacked bar plot")
		text = get_text(mode)
		plot_builder(mode, text.lower(), data)
	return get_cmd(mode)

def plot_builder(mode, plot_type, data):
	if plot_type == 'distribution plot':
		gen_output(mode,"Hold on while I generate the plot")
		distributionplot(data)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return
	elif plot_type == 'pair plot':
		gen_output(mode,"Hold on while I generate the plot")
		pairplot(data)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return
	elif plot_type == 'scatter plot':
		print(data.columns.values)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select the X column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"X column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode, 'Please select the Y column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			gen_output(mode,"Y column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		scatterplot(X, Y)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	elif plot_type == 'line plot':
		print(data.columns.values)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select the X column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"X column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode, 'Please select the Y column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			gen_output(mode,"Y column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		lineplot(X, Y)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	elif plot_type == 'histogram':
		print(data.columns.values)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select a column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"Column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		histogram(X)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	elif plot_type == 'overlaid histogram':
		for col in data.columns.values:
			if data[col].dtype!='object':
				print(col)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select the X column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"X column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode, 'Please select the Y column from the list off column names')
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			gen_output(mode,"Y column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		overlaid_histogram(X, Y)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	elif plot_type == 'bar plot':
		print(data.columns.values)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select the X column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"X column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode, 'Please select the Y column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			gen_output(mode,"Y column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		barplot(X, Y)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	elif plot_type == 'stacked bar plot':
		print(data.columns.values)
		col_names = list(data.columns.values)
		gen_output(mode, 'Please select the X column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			X = data[col]
			gen_output(mode,"X column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode, 'Please select the Y column from the list of column names')
		col = get_text(mode)
		if col in col_names:
			Y = data[col]
			gen_output(mode,"Y column set")
		else:
			gen_output(mode,"Column not found")
			plot_builder(mode, plot_type, data)
		gen_output(mode,"Hold on while I generate the plot")
		stackedbarplot(X, Y)
		gen_output(mode,"Do you want me to generate more plots?")
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_visualize(mode, 0, data)
		else:
			return
		return

	else: 
		print("No plots selected")
		return get_cmd(mode)	
	return get_cmd(mode)

def cmd_build_model(mode, model_type, data):
	gen_output(mode,"Before I build a model for you, please choose the label column.")
	print(data.columns.values)
	col_names = list(data.columns.values)
	col = get_text(mode)
	if col in col_names:
		Y = data[col]
		gen_output(mode,"Label column set")
	else:
		gen_output(mode,"Rebuild the model")
		cmd_build_model(mode, model_type, data)
	X = data.drop(col, axis = 1)
	gen_output(mode,"Below are the first 5 features: ")
	print(X.head())
	gen_output(mode,"Below are the first 5 labels: ")
	print(Y.head())
	if model_type != 0:
		model_builder(mode, model_type, X, Y)
	else:
		gen_output(mode,"Choose one model from the list: ")
		print("1. Logistic Regression model")
		print("2. K Neighbors Classifier model")
		print("3. Decision Tree Classifier model")
		print("4. Gaussian NB model")
		print("5. Support Vector Classifier model")
		cmd, model_type = get_cmd(mode)
		model_builder(mode, model_type, X, Y)
	return get_cmd(mode)
	
def model_builder(mode, model_name, X, Y):
	if model_name == 'LR':
		gen_output(mode,"Hold on let me build the model for you.")
		build_model('Logistic Regression model', X, Y)
		gen_output(mode,"Done! I have also saved a copy of the model for you.")
	elif model_name == 'KNN':
		gen_output(mode,"Hold on let me build the model for you.")
		build_model('K Neighbors Classifier', X, Y)
		gen_output(mode,"Done! I have also saved a copy of the model for you.")
	elif model_name == 'CART':
		gen_output(mode,"Hold on let me build the model for you.")
		build_model('Decision Tree Classifier', X, Y)
		gen_output(mode,"Done! I have also saved a copy of the model for you.")
	elif model_name == 'NB':
		gen_output(mode,"Hold on let me build the model for you.")
		build_model('Gaussian NB', X, Y)
		gen_output(mode,"Done! I have also saved a copy of the model for you.")
	elif model_name == 'SVC':
		gen_output(mode,"Hold on let me build the model for you.")	
		build_model('Support Vector Classifier', X, Y)
		gen_output(mode,"Done! I have also saved a copy of the model for you.")
	else:
		return cmd_build_model(mode, model_type, data)
	
def cmd_data_exploration(mode,data):
	print('**********************************************************')
	gen_output(mode,'How can I help you explore the data?')
	explore_type,row_num = get_cmd(mode)
	if explore_type == 'head':
		gen_output(mode,'Here are the top rows: ')
		print(data.head(row_num))
		gen_output(mode,'Do you want to continue?')
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_data_exploration(mode,data)
		else:
			return
		return 
	elif explore_type == 'tail':
		gen_output(mode,'Here are the bottom rows: ')
		print(data.tail(row_num))
		gen_output(mode,'Do you want to continue?')
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_data_exploration(mode,data)
		else:
			return
		return 
	elif explore_type == 'distribution':
		print(data.describe())
		gen_output(mode,'Do you want to continue?')
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_data_exploration(mode,data)
		else:
			return
		return 
	elif explore_type == 'data type':
		count = data.dtypes.value_counts() 
		for i in count.index: print('The number of ', i, 'objects is ', count[i])
		gen_output(mode,'Do you want to continue?')
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_data_exploration(mode,data)
		else:
			return
		return 
	elif explore_type == 'unique':
		for col in data.columns.values:
			if data[col].dtype=='object':
				print('*************************************************************************')
				print("Unique value in",col, "is: ",data[col].unique())
				print('*************************************************************************')
		gen_output(mode,'Do you want to continue?')
		text = get_text(mode)
		if text.lower() == 'yes':
			return cmd_data_exploration(mode,data)
		else:
			return
		return 
	elif explore_type == 'missing':
		if data.isnull().values.any() == True:
			null_col = data.isnull().sum(axis = 0)
			null_col[null_col != 0]
			gen_output(mode,'Do you want to continue?')
			text = get_text(mode)
			if text.lower() == 'yes':
				return cmd_data_exploration(mode,data)
			else:
				return
			return 
		else:
			gen_output(mode,"Dataset is already clean.")
			gen_output(mode,'Do you want to continue?')
			text = get_text(mode)
			if text.lower() == 'yes':
				return cmd_data_exploration(mode,data)
			else:
				return
			return 
	return get_cmd(mode)
	
# ********************** Initiate Anna **********************

print("************* Initiating Anna *************")
engine.say("Initiating Anna")
engine.runAndWait()
time.sleep(2)
gen_output('VOICE',"Hello! I am Anna, your personal data analysis assistant. I can help you analyze your data and build machine learning models.")
 
mode = get_mode()
username = askUser(mode)
welcome_user(mode)

try:
	while True:
		cmd, model_type = get_cmd(mode)
		if cmd == '1U':
			data = cmd_upload_data(mode)
		elif cmd == '4F':
			cmd_features(mode)
		elif cmd == '2D':
			cmd_describe_data(mode, data)
		elif cmd == '3C':
			data = cmd_clean_data(mode, data)		
		elif cmd == '5V':
			cmd_visualize(mode, model_type, data)
		elif cmd == '6B':
			cmd_build_model(mode, model_type, data)
		elif cmd == '7E':
			cmd_data_exploration(mode,data)
		elif cmd == 'bye':
			engine.say("Thank you for using me.")
			print("Thank you for using me.")
			engine.runAndWait()
			sys.exit()
		else:
			get_cmd(mode)
			
except Exception as e: print(e)
	#engine.say("Exception triggered")
	#print("Exception triggered")
	#Exception as e: print(e)
		
