# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 02:18:38 2023

@author: Stiana Fernandes
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <---format of read_csv
#pandas is a library, read_csv is a function

data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv', sep=";")

#Here seperator is included to show that semicolon is used instead of comma since file is comma separated
#check separator in variable section 
#do it when table is not formed correctly with rows and columns



#Summary of the dataset:
data.info()

#Playing with variables:

var= ['apple','pear','kiwi'] #SQUARE BRACKETS - LIST CAN CHANGE ITEMS IN IT - LISTS
var= ('apple','pear','kiwi') #ROUND BRACKETS - CAN NOT CHANGE ITEMS IN IT - TUPLES
var= range(10)
var = {'name':'Dee', 'Location' : 'South Africa'} #Dictionary has Keys
var = {'apple','pear','kiwi'} #Set
var = True

#Working with Calculations:
    
#Defining Variables:

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased =  6

#Mathematical Operations:
    
ProfitPerItem = 21.11 - 11.73 
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction = NumberOfItemsPurchased*CostPerItem

#variable = df['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberOfItemsPurchased

#adding a new column to df
data['CostPerTransaction'] = CostPerItem*NumberOfItemsPurchased
#OR data['CostPerTransaction'] = data['CostPerItem']*data['NumberOfItemsPurchased']

#SalesPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Profit and Markup Calculation
#Profit = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


#Markup = (Sales-Cost)/Cost *100
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#Rounding Markup
roundmarkup = round(data['Markup'],2)

data['Markup'] = roundmarkup

#combining datafields

my_name = 'stiana' + 'fernandes'
my_date = 'Day' + 'Month' + 'Year'

my_date = data['Day'] + '-' #Doesn't work because can't concat string and integer dtype

#Checking Cols datatype

print(data['Day'].dtype)
#Change dtype

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['Date'] = day + '-' + data['Month'] + '-' + year

#Using iloc to view specific rows/cols

data.iloc[0] #Views the row with index 0
data.iloc[0:3] #Views first 3 rows 
data.iloc[-5:] #Views last 5 rows
data.head(5) #Brings in first 5 rows
data.iloc[:,2] #Full of 2nd col
data.iloc[4,2] #4th row, 2nd col

#Using split for ClientKeywords Field

#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

#Creating new cols in df using split_col

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Using Replace Function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

# Using lower function to change col data to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#Merging files by joining data

season_data = pd.read_csv('value_inc_seasons.csv', sep = ';')
#merging files: merge_df = pd.merge(df_old, df_new, on = 'Key'

data = pd.merge(data, season_data, on = 'Month')

#Dropping Cols

#df = df.drop('Column_Name', axis=1)
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Month','Year'], axis=1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False) #Because we don't want Index included, if want put True









