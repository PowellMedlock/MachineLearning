import numpy as np
import pandas as pd

# a. Using Numpy create random vector of size 15 having only integers in range 1-20
# 1. reshape the array to 3,5
# 2. print array shape
# 3. Replace the max in each row with 0
np.random.seed()
a = np.random.randint(1, 20, 15, int)
a = np.reshape(a, (3, 5))
print(np.shape(a))
a[np.arange(len(a)), np.argmax(a, axis=1)] = 0
print(a)
print('\n')

# b. Write a program to compute the eigenvalues and eigenvectors of the square array given
print("calculating eigenvalues and eigenvectors")
b = [3, -2, 1, 0]
b = np.reshape(b, (2, 2))
eVal = np.linalg.eig(b)
print(eVal)
print('\n')

# c. calculate the sum of the diagonal elements of a given array

c = [0, 1, 2, 3, 4, 5]
c = np.reshape(c, (2, 3))
c = np.trace(c)
print("Diagonal sum: ")
print(c)
print('\n')


# d. Write a numpy program to create a new shape to an array without changing its data
def reshape2(array):
    newArray = np.reshape(array, (1, np.size(array)))
    return newArray

array1 = [7,7],[3,3],[2,2]
reshape2(array1)
print(array1)
print('\n')
# Read the provided CSV file ‘data.csv’.
df = pd.read_csv('/home/somedgnrte/data.csv')

# Show the basic statistical description about the data.
print('Show the basic statistical description about the data.')
print(df.describe())
# Check if the data has null values.
print('Check if the data has null values.')
print(df.isnull().values.any())
print('\n')
# Replace the null values with the mean
print('Replace the null values with the mean')
df.fillna(df.mean(), inplace=True)
print(df)
print(df.isnull().values.any())
print('\n')
# elect at least two columns and aggregate the data using: min, max, count, mean.
print('elect at least two columns and aggregate the data using: min, max, count, mean.')
var = df.loc[[7, 8]]
print(var)
print('\n')
var2 = df.loc[[7, 8]].min()
print(var2)
print('\n')
var3 = df.loc[[7, 8]].max()
print(var3)
print('\n')
var4 = df.loc[[7, 8]].count()
print(var4)
print('\n')
var5 = df.loc[[7, 8]].mean()
print(var5)
print('\n')
# Filter the dataframe to select the rows with calories values between 500 and 1000.
print('Filter the dataframe to select the rows with calories values between 500 and 1000.')
cal = df.loc[(500 < df['Calories']) & (df['Calories'] < 1000)]
print(cal)
print('\n')
# Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print('Filter the dataframe to select the rows with calories values > 500 and pulse < 100.')
calAndPulse = df.loc[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(calAndPulse)
print('\n')
# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = df.drop('Maxpulse', axis=1)
print(df_modified)
print('\n')
# Delete the “Maxpulse” column from the main df dataframe
del df["Maxpulse"]
print(df)
print('\n')
# Convert the datatype of Calories column to int datatype.
print(df.dtypes)
df['Calories'] = df['Calories'].astype(int)
print(df.dtypes)
