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
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import classification_report
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

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
	ncols = len(data.columns)
	fig, axes = plt.subplots(ncols -1)
	plt.subplots_adjust(hspace = 1.5)
	for ax, col in zip(axes, data.columns):
		sns.distplot(data[col], ax=ax)
	#plt.figure(3)
	sns.pairplot(data)
	#sns.heatmap(data)
	plt.show()

#def build_model(name, model, X, Y):
#	results = []
#	names = []
#	seed = 7
#	scoring = 'accuracy'
#	validation_size = 0.20
#	X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
#	kfold = model_selection.KFold(n_splits=10, random_state=seed)
#	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
#	results.append(cv_results)
#	names.append(name)
#	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#	print(msg)

def build_model(name, X, Y):
	validation_size = 0.20
	if type(Y) != str:
		Y = Y.astype('str')
	X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=1001)
	if name in ('Logistic Regression model'):
		clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial', max_iter=1000)
	elif name in ('K Neighbors Classifier'):
		clf = KNeighborsClassifier()
	elif name in ('Decision Tree Classifier'):
		clf = DecisionTreeClassifier()
	elif name in ('Gaussian NB'):
		clf = GaussianNB()
	elif name in ('Support Vector Classifier'):
		clf = SVC(gamma='scale')
	clf.fit(X_train, Y_train)
	print('*'*100)
	print('Model name: ', name)
	print('*'*100)
	print(clf)
	print('*'*100)
	print("Score for training dataset: ", clf.score(X_train, Y_train))
	print('*'*100)
	Y_pred = clf.predict(X_validation)
	print('Predicted values: ', Y_pred)
	print('*'*100)
	print('Classification Report')
	print(classification_report(Y_validation, Y_pred, target_names=list(Y.unique())))
	print('*'*100)
	title = "Learning Curves"
	plot_learning_curve(clf, title, X_train, Y_train, ylim=(0.7, 1.01), cv=5, n_jobs=4)
	filename = 'Final_model_by_Anna.sav'
	pickle.dump(clf, open(filename, 'wb'))

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
						n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Training examples")
	plt.ylabel("Score")
	train_sizes, train_scores, test_scores = learning_curve(
		estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
	train_scores_mean = np.mean(train_scores, axis=1)
	train_scores_std = np.std(train_scores, axis=1)
	test_scores_mean = np.mean(test_scores, axis=1)
	test_scores_std = np.std(test_scores, axis=1)
	plt.grid()

	plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
					 train_scores_mean + train_scores_std, alpha=0.1,
					 color="r")
	plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
					 test_scores_mean + test_scores_std, alpha=0.1, color="g")
	plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
			 label="Training score")
	plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
			 label="Cross-validation score")

	plt.legend(loc="best")
	plt.show()