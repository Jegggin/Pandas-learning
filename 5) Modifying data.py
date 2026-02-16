# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:38:38 2024

@author: josep

5) Modifying data
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


#can change collumn names by setting df.columns = ['names you want'], bu this is not a practical method

people_caps = df_people
people_caps.columns = [x.upper() for x in people_caps.columns]
people_caps.columns.str.replace(' ', '_') #replaces spaces with underscore

#another renaming method
df_people.rename(columns={'FIRST':'first_name', 'LAST':'last_name'},inplace=True) #needs inplace

#replacing a row of data
df_people.loc[2] = ['John', 'Smith', 'newemail']

#replacing data in row with selected columns
df_people.loc[2, ['last_name','EMAIL']] = ['Doe', 'ogemail']

#df.[XXX].replace({...}) can be used for this as well, don't use df.map

#change multiple rows
email_low = df_people
email_low['EMAIL'] = email_low['EMAIL'].str.lower()

#count characters in a row
#NOTE that using .apply(len) on a whole data frame counts the element in each series (each column), so coutns the number of rows basically
#To change from couting rows to collumns, put .apply(len, axis='columns')
count = df_people['EMAIL'].apply(len)
count_all = df.applymap(len) #counts number of letters in all elements

#applymap() applies something to all elements

#using functions with .apply()
#can use lambda functions for this, just put the lambda instead of the defined function
def update_email(email):
    return email.upper()

email_up = email_low
email_up['EMAIL'] = email_up['EMAIL'].apply(update_email)

#finding minimum values, can work with numbers and strings
min_people = df_people.apply(pd.Series.min) #finds elements begining with lowest alphabet letter from each series

