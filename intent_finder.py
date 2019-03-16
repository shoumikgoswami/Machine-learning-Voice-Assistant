from wit import Wit
import pandas as pd

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
	client = Wit('UXH7HZWOS3WUFCZHOH3WYDUSM3ZIJG26')
	intent = client.message(text)
	plot_type = 0
	model_type = 0
	if ('model' in intent['entities'].keys()) & ('intent' in intent['entities'].keys()):
		command_type, model_type = intent['entities']['intent'][0]['value'], intent['entities']['model'][0]['value']
	elif ('model' in intent['entities'].keys()) & ('intent' not in intent['entities'].keys()):
		command_type, model_type = 0, intent['entities']['model'][0]['value']
	elif ('plot_type' in intent['entities'].keys()) & ('intent' in intent['entities'].keys()):
		command_type, plot_type = intent['entities']['intent'][0]['value'], intent['entities']['plot_type'][0]['value']
	elif ('plot_type' in intent['entities'].keys()) & ('intent' not in intent['entities'].keys()):
		command_type, model_type = 0, intent['entities']['plot_type'][0]['value']
	elif ('bye' in intent['entities'].keys()) & ('intent' not in intent['entities'].keys()):
		command_type, model_type = intent['entities']['bye'][0]['value'], 0
	elif ('explore' in intent['entities'].keys()) & ('intent' not in intent['entities'].keys()):
		explore_type =  intent['entities']['explore'][0]['value']
		if ('number' in intent['entities'].keys()):
			row_num = intent['entities']['number'][0]['value']
		else:
			row_num = 0
		command_type = ''
		model_type = ''
		plot_type = ''
	else:
		command_type, model_type = intent['entities']['intent'][0]['value'], 0
	if command_type == 'upload data':
		cmd = '1U'
	elif command_type == 'describe data':
		cmd = '2D'
	elif command_type == 'clean data':
		cmd = '3C'
	elif command_type == 'features':
		cmd = '4F'
	elif command_type == 'visualize':
		cmd = '5V'
	elif command_type == 'build model':
		cmd = '6B'
	elif command_type == 'data exploration':
		cmd = '7E'
	elif model_type != 0:
		cmd = 'model'
	elif plot_type != 0:
		cmd = 'plot'    
	elif command_type == 'true':
		cmd = 'bye'
	else:
		cmd = 'error'
	if model_type == 'logistic regression':
		model_type = 'LR'
	elif model_type == 'knn classifier':
		model_type = 'KNN'
	elif model_type == 'decision tree classifier':
		model_type = 'CART'
	elif model_type == 'gaussian nb':
		model_type = 'NB'
	elif model_type == 'svm classifier':
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