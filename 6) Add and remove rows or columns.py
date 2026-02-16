# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:58:55 2024

@author: josep

6) Add/remove rows/columns
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

df_people['full_name'] = df_people['first'] + ' ' + df_people['last']

df_email = df_people.drop(columns=['first','last'])

df_seperated = df_people['full_name'].str.split(' ', expand = True) #splits on space by default, try expand = False

