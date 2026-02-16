# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:39:16 2024

@author: josep

This details how to use Pandas. This is a data analysis module so will likely be
useful for your programming purposes.
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

