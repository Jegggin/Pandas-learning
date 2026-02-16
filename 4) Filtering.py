# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:37:59 2024

@author: josep

4) Filtering

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


#Can test for certain values by using df['column name'] == 'string' and get True/False for each row

#method 1
filt = df_people['last'] == 'Doe'
people_filt = df_people[filt] #can both be on same line

#method 2
people_filt_2 = df_people.loc[filt,'email']

# and/or statements

#NOTE THE & SYMBOL
filt_and = (df_people['last'] == 'Doe') & (df_people['first'] == 'John')

#NOTE THE | SYMBOL
filt_or = (df_people['last'] == 'Doe') | (df_people['first'] == 'John')

#to do the inverse of the filter (NOTE THE ~ SYMBOL)
people_filt_2_rev = df_people.loc[~filt,'email']

#example using the large data set
high_salary_filt = (df['ConvertedComp'] > 70000)
high_salary = df.loc[high_salary_filt, ['Country', 'LanguageWorkedWith','ConvertedComp']]

#filter out certain countries
countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
country_filt = df['Country'].isin(countries)
high_salary_2 = df.loc[(high_salary_filt & country_filt), ['Country', 'LanguageWorkedWith','ConvertedComp']]

#find out if respondent worked with python
language_filt = df['LanguageWorkedWith'].str.contains('Python', na=False) #remember the end bit, it filters  out NaN values
know_python = df.loc[language_filt, 'LanguageWorkedWith']
