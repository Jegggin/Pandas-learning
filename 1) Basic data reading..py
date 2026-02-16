# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:33:14 2024

@author: josep
'''
1) Basic data reading.
'''
"""

import pandas as pd

df = pd.read_csv('pandas_data/survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('pandas_data/survey_results_schema.csv',index_col='Column') #schema is like an index?

people = {
    "first": ["Corey",'Jane','John'],
    "last": ["Schafer",'Doe','Doe'],
    "email": ["email1",'email2','email3']
}

df_people = pd.DataFrame(people)

'''
#df.shape [no parentheses () needed] gives the dimensions of the data frame

#df.info() gives dimensions and data types of the collumns (needs parentheses)

#df.head() gives first five rows by default, can specify a number of rows in the parentheses
 
#df.tail() does the same with the last rows
'''

pd.set_option('display.max_columns',85) #set to whatever you want
pd.set_option('display.max_rows',85) #set to whatever you want



'''
Creating data frames from dictionaries:
'''



