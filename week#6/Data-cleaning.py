
################ Data cleaning the Iris dataset #################
from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load iris dataset
iris = datasets.load_iris()

# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
# data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

# data cleaning step #1 - check missing/null values

#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data
cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines
x = iris_df.isnull().sum()
y = iris_df.isnull().mean()

iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

print(f"Number of missing values: {x}")
print(f"Mean of missing values: {y}")

# data cleaning step #2 - check duplicate data

# Add the target column for completeness
data['target'] = iris.target

# Check for duplicate rows
duplicates = data[data.duplicated()]

print(f"Number of duplicate rows: {len(duplicates)}")
print("Duplicate rows:")
print(duplicates)


# data cleaning step #3 - determine the unusual data (outliers)



### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description

df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation matrix:\n", correlation_matrix)

# Create a heatmap for better visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Iris Dataset Features')
plt.show()


