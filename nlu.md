

## intent:upload_data
- upload data
- upload data set
- can you upload the data
- load the data

## intent:describe_data
- describe the data
- describe the dataset
- describe data

## intent: clean_data
- clean the data
- clean the dataset
- remove nan values from the data
- remove nan values
- remove null values
- drop nan values
- drop null values
- remove nan values from all rows

## intent: features
- what are your features
- tell me what you can do
- what can you do
- what all functions can you perform

##intent: visualize
- visualize the data
- generate plots
- create plots
- Generate [distribution plot](plot_type)
- can you create [distribution plot](plot_type)
- create [distribution graph](plot_type)
- Generate [pair plot](plot_type)
- can you create [pair plot](plot_type)
- create [pair plot](plot_type)
- Generate [scatter plot](plot_type)
- can you create [scatter plot](plot_type)
- create [scatter plot](plot_type)
- Generate [line plot](plot_type)
- can you create [line plot](plot_type)
- create [line graph](plot_type)
- Generate [histogram](plot_type)
- can you create [histogram](plot_type)
- create [histogram](plot_type)
- Generate [overlaid histogram](plot_type)
- can you create [overlaid histogram](plot_type)
- create [overlaid histogram](plot_type)
- Generate [bar plot](plot_type)
- can you create [bar plot](plot_type)
- create [bar graph](plot_type)
- Generate [stacked bar plot](plot_type)
- can you create [stacked bar plot](plot_type)
- create [stacked bar graph](plot_type)

## synonym:distribution plot
- distribution graph
- distribution chart

## synonym:pair plot
- pair chart
- pair graph

## synonym:scatter plot
- scatter graph
- scatter chart

## synonym:line plot
- line graph
- line chart

## synonym:histogram
- histogram chart
- histogram graph

## synonym:overlaid historgram
- overlaid histogram chart
- overlaid histogram graph

## synonym:bar plot
- bar graph
- bar chart

## synonym:stacked bar plot
- stacked bar graph
- stacked bar chart

## lookup: plot_type
- distribution plot
- pair plot
- scatter plot
- line plot
- histogram
- overlaid historgram
- bar plot
- stacked bar plot

## intent: build_model
- Build model
- Build machine learning model
- Build a classifier
- Generate model
- Can you build a [k neighbors](model_name) classifier        
- Create [logistic regression](model_name) model
- build [gaussian nb](model_name) model
- build [support vector](model_name) model
- build [decision tree](model_name) model
- build [decision tree](model_name) classifier


## lookup: model_name
- logisitic regression
- k neighbors classifier
- decision tree classifier
- gaussian nb classifier
- support vector classifier

## synonym:kneighbors
- knn
- k nearest neighbours
- k nearest neighbors
- KNN
- K-NN
- k neighbors

## synonym:support vector
- svm
- svc
- support vector machines

## intent:data_exploration
- explore the data
- can you help me explore the dataset
- help me explore the data
- show me [top](head) [5](number) rows
- show me [first](head) [10](number) rows
- show me [bottom](tail) [3](number) rows
- show the [top](head) [three](number) rows
- show me [last](tail) [7](number) rows
- load the [first](head) [five](number) rows
- can you show me the [last](tail) [ten](number) rows
- Show the [data distribution](data_distribution)
- [Data distribution](data_distribution)
- can you show the [distribution](data_distribution) of the data
- Show the different [data types](data_type) in the dataset
- Show the [data types](data_type)
- [Data types](data_type)
- what are the different [types of data](data_type)
- Show me the [unique](unique) values in the dataset
- Show me the [unique values](unique)
- [Unique](unique) values
- what are the [unique rows](unique) in the data
- Show me columns with [missing](missing) values
- [Missing values](missing)
- Columns with [missing](missing) values
- show the columns with [missing](missing) values

## regex: number
- [0-9]+

