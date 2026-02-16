# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:36:32 2024

@author: josep

3) More on indices (see above how to set index when reading in files)

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


df_emails = df_people.set_index('email') #can set index like this too

sorted_schema = schema_df.sort_index(inplace=True) #self explanatory what this does, try it in consol
#not exactly sure what inplace does but I think it's useful?

sorted_schema_reverse = schema_df.sort_index(ascending = False) #can do this too

