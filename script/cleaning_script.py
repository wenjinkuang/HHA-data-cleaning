import pandas as pd
import datetime as dt
import uuid 
import numpy as np

################## DATA CLEANING ##################

## loading in the original data
df = pd.read_csv(r'data\School_Learning_Modalities.csv')

## printing data to check if it loaded properly 
df

## prints the counts of amount of columns and rows 
df.shape 

## prints the columns names 
list(df)
column_names = list(df) ## assigning the variable column_names to show the name of the columns

## remove all special characters and whitespace ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 

## check to see if strings are strings, number are numbers, dates are dates, and boolean are booleans
df.dtypes
# create a list of columns that are strings, and save as strings 
strings = df.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = df.select_dtypes(include=['int64', 'float64']).columns
# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = df.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns

## converting the week column from type(object) to type(datetime) in the format of '%Y_%M_%D'
df['Week'] = pd.to_datetime(df['Week'], format='%Y_%M_%D')
## changing the title of the 'Week' column to 'Week of', since the dates are a week apart 
df = df.rename(columns={'Week':'Week_of'})

## looking for duplicated values and removing duplicated values 
df.duplicated()
df.duplicated().sum() ## count of duplicates 
df.drop_duplicates() ## dropping duplicated values

## count of missing values per column 
df.isnull().sum()
# replacing blank, empty cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)

## adding a new column with a function based on the 'Learning_Modality' column where if it's 'In Person' its True if it's 'Remote/Hybrid' its False
def modality_inperson(contact):
    if contact == 'In Person':
        return 'True'
    else:
        return 'False'
df['modality_inperson'] = df['Learning_Modality'].apply(modality_inperson)
df ## checking if the new column was added 

## saving the new column into a different .CSV file 
df.to_csv(r'data\School_Learning_Modalities_Cleaned.csv')