import pandas as pd
from tkfilebrowser import askopenfilenames
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")

def loaddata():
	rep = askopenfilenames(initialdir='/', initialfile='tmp',
						   filetypes=[("All files", "*")])
	data = pd.read_csv(rep[0])
	data.columns = map(str.lower, data.columns)
	return data

def describedata(data):
	print("Number of rows: ", data.shape[0])
	print("Number of columns: ", data.shape[1])
	print(data.info())

def generategraphs(data):
	#plt.figure(1)
	#data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
	#plt.figure(2)
	#data.hist()
	#plt.figure(3)
	#scatter_matrix(data)
	#plt.figure(1).show()
	#plt.figure(2).show()
	sns.pairplot(data)
	plt.show()

def build_model(name, model, X, Y):
	results = []
	names = []
	seed = 7
	scoring = 'accuracy'
	validation_size = 0.20
	X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
