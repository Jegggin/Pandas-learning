# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:35:25 2024

@author: josep
'''
2) Slicing data frames
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

#can access individual row by using people(first/last/email)

'''
#can ACCESS INDIVIDUAL COLLUMNS with df['first/second/email'] or just df.email


#can ACCESS MULTIPLE COLLUMNS with df[['last','first']] (remember both brackets)


#can LOCATE ROWS by using df.iloc[i], i being the index this accesses an individual
row and gives it as a series.


#df.loc[i] locates a ROW BY USING AN INDEX LABEL (will be detailed later), basically
you don't have to use intiger indices but use the row/collumn labels


NOTE: to SEE A FULL LINE, specify the desired collumn as well as the row


#df['xxxx'].value_counts() COUNTS THE NUMBER OF EACH RESPONSE in the collumn


#df.collumns and df.rows gives a LIST OF ALL ROW AND COLLUMN labels in the data frame
'''

#example
df_hobbyist = df['Hobbyist'] #try counting each response

df_hobbyist_rows = df.loc[[1,2,3],'Hobbyist']

df_multiple_collumns = df.loc[1:3, 'Hobbyist':'Employment']

