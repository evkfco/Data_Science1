import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset
url= 'https://raw.githubusercontent.com/evkfco/Data_Science1/refs/heads/main/n_movies.csv'
df = pd.read_csv(url)
# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Delete every rows with missing values
df_cleaned = df.dropna()
print("After removing missing values:")
print(df_cleaned.isnull().sum())

#Delete 'description' column and change star list to number of stars
df_cleaned = df_cleaned.drop(columns=['description'])
df_cleaned = df_cleaned.drop(columns=['year'])
df_cleaned['stars'] = df_cleaned['stars'].apply(lambda x: len(str(x).split(',')))
df_cleaned['votes'] = df_cleaned['votes'].str.replace(',', '').astype(int)
df_cleaned['duration'] = df_cleaned['duration'].str.replace(' min', '').astype(int)
# Display the cleaned dataframe info
print(df_cleaned.head())
print(df_cleaned.info())

# Save the cleaned dataframe to a new CSV file
df_cleaned.to_csv('n_movies_cleaned.csv', index=False)
