from rasa_nlu.model import Interpreter
from word2number import w2n
import pandas as pd
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
tf.logging.set_verbosity(tf.logging.ERROR)
''' Code List

Upload data = 1U
Describe data = 2D
Clean data = 3C
Features = 4F
Visualize = 5V
Build model = 6B

Models - 
logistic regression
knn classifier
decision tree classifier
gaussian nb
svm classifier

'''
def get_intent(text):
	command_type = ''
	model_type = 0
	plot_type = 0
	explore_type = ''
	row_num = 0

	interpreter = Interpreter.load("./models/nlu/default/tensor")
	intent = interpreter.parse(text)
	
	if intent['intent']['confidence']>0.60:
		command_type = intent['intent']['name']
		if len(intent['entities']) == 0:
			model_type = 0
			plot_type = 0
		elif len(intent['entities']) == 1:
			if intent['entities'][0]['entity']=='plot_type':
				plot_type = intent['entities'][0]['value']
				model_type = 0
			elif intent['entities'][0]['entity']=='model_name':
				model_type = intent['entities'][0]['value']
				plot_type = 0
			else:
				explore_type = intent['entities'][0]['entity']
				model_type = 0
				plot_type = 0
				command_type = ''
		elif len(intent['entities']) == 2:
			explore_type = intent['entities'][0]['entity']
			row_num = w2n.word_to_num(intent['entities'][1]['value'])
			model_type = 0
			plot_type = 0
			command_type = ''
	else:
		command_type = 'error'

	if command_type == 'upload_data':
		cmd = '1U'
	elif command_type == 'describe_data':
		cmd = '2D'
	elif command_type == 'clean_data':
		cmd = '3C'
	elif command_type == 'features':
		cmd = '4F'
	elif command_type == 'visualize':
		cmd = '5V'
	elif command_type == 'build_model':
		cmd = '6B'
	elif command_type == 'data_exploration':
		cmd = '7E'
	elif (model_type != 0) & (command_type != 'error'):
		cmd = 'model'
	elif (plot_type != 0) & (command_type != 'error'):
		cmd = 'plot'    
	elif command_type == 'error':
		cmd = 'error'    
	else:
		cmd = 'error'  
	if model_type == 'logistic regression':
		model_type = 'LR'
	elif model_type == 'kneighbors':
		model_type = 'KNN'
	elif model_type == 'decision tree':
		model_type = 'CART'
	elif model_type == 'gaussian nb':
		model_type = 'NB'
	elif model_type == 'support vector':
		model_type = 'SVC'
	else:
		model_type = 0
		
	with open("log.txt", 'a+') as textfile:
		if len(command_type)>0:
			textfile.write('\n' + text + '\t' + '|' + '\t' + command_type)
		elif (len(explore_type)>0) & (len(command_type)==0):
			textfile.write('\n' + text + '\t' + '|' + '\t' + explore_type)
	
	if len(command_type)>0:
		if (plot_type == 0):
			return cmd, model_type
		elif (model_type == 0) & (plot_type != 0):
			return cmd, plot_type
	elif (len(explore_type)>0) & (len(command_type)==0):
		return explore_type, row_num