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

def distributionplot(data):
	#plt.figure(1)
	#data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
	#plt.figure(2)
	ncols = len(data.columns)
	fig, axes = plt.subplots(ncols -1)
	plt.subplots_adjust(hspace = 1.5)
	for ax, col in zip(axes, data.columns):
		sns.distplot(data[col], ax=ax)
	#plt.figure(3)
	plt.show()

def pairplot(data):
	sns.pairplot(data)
	#sns.heatmap(data)
	plt.show()

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

def scatterplot(x_data, y_data, yscale_log=False):
 
	x_label = x_data.name
	y_label = y_data.name
	title="Scatter plot"  


	# Create the plot object
	_, ax = plt.subplots()

	# Plot the data, set the size (s), color and transparency (alpha)
	# of the points
	ax.scatter(x_data, y_data, s = 10, alpha = 0.75)

	if yscale_log == True:
		ax.set_yscale('log')

	# Label the axes and provide a title
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.set_title(title)
	ax.legend(loc = 'best')
	plt.show()

def lineplot(x_data, y_data):
	# Create the plot object
	x_label = x_data.name
	y_label = y_data.name
	_, ax = plt.subplots()

	# Plot the best fit line, set the linewidth (lw), color and
	# transparency (alpha) of the line
	ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

	# Label the axes and provide a title
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.set_title('Line plot')
	ax.legend(loc = 'best')
	plt.show()

def histogram(data, cumulative=False):
	_, ax = plt.subplots()
	ax.hist(data, cumulative = cumulative)
	x_label = data.name
	ax.set_xlabel(x_label)
	ax.set_title('Histogram')   	
	ax.legend(loc = 'best')
	plt.show()

def overlaid_histogram(data1, data2, data1_color="#539caf", data2_color="#7663b0"):
	# Set the bounds for the bins so that the two distributions are fairly compared
	x_label = data1.name
	y_label = data2.name
	max_nbins = 10
	n_bins = 0
	data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
	binwidth = (data_range[1] - data_range[0]) / max_nbins

	if n_bins == 0:
		bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
	else: 
		bins = n_bins

	# Create the plot
	_, ax = plt.subplots()
	ax.hist(data1, bins = bins, color = data1_color, alpha = 1, label = x_label)
	ax.hist(data2, bins = bins, color = data2_color, alpha = 0.75, label = y_label)
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	ax.set_title('Overlaid Histogram')
	ax.legend(loc = 'best')
	plt.show()

def barplot(x_data, y_data):
	x_label = x_data.name
	y_label = y_data.name
	_, ax = plt.subplots()
	# Draw bars, position them in the center of the tick mark on the x-axis
	ax.bar(x_data, y_data, color = '#539caf', align = 'center')
	# Draw error bars to show standard deviation, set ls to 'none'
	# to remove line between points
	#ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	ax.set_title('Bar plot')
	plt.show()



def stackedbarplot(x_data, y_data):

	x_label = x_data.name
	y_label = y_data.name
	y_data_list = list(y_data.unique())
	_, ax = plt.subplots()
	# Draw bars, one category at a time
	for i in range(0, len(y_data_list)):
		if i == 0:
			ax.bar(x_data, y_data_list[i], align = 'center', label = y_data_list[i])
		else:
			# For each category after the first, the bottom of the
			# bar will be the top of the last category
			ax.bar(x_data, y_data_list[i], bottom = y_data_list[i - 1], align = 'center', label = y_data_list[i])
	ax.set_ylabel(y_label)
	ax.set_xlabel(x_label)
	ax.set_title('Stacked Bar plot')
	ax.legend(loc = 'upper right')
	plt.show()
