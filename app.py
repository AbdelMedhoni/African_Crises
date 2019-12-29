import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json


dataPath = 'accData.json'

accidentsDf =pd.read_json(dataPath,orient=None,typ='frame',dtype=dict)

accidentsDf.set_index('Accident_Index')

'''accidentsDf.loc[(accidentsDf.Vehicle_Category == 'Taxi') & (accidentsDf.Vehicle_Manoeuvre == 'Turning right') ]

accidentsDf.drop('Vehicle_Category', axis=1).plot(kind='box', subplots=True,layout=(2,2), sharex=False, sharey=False, figsize=(9,9), title='Box Plot for each input variable')
'''

def classifier(df,criteria,value):
    return df.loc[(accidentsDf[criteria] == value)]



def numberofAccients(df):
    return df.Accident_Index.count()
''' Listing numbers of accidents per Vehicle Category
for ac in accidentsDf.Vehicle_Category.unique():
    x = numberofAccients(classifier(accidentsDf,"Vehicle_Category",ac))
    print(ac + " accidents are " + str(x) )

'''

'''Listing numbers of accidents per Vehicle Category
for ac in accidentsDf.Month_of_Year.unique():
    x = numberofAccients(classifier(accidentsDf,"Month_of_Year",ac))
    print(" Month: " + str(ac) + " accidents are " + str(x) )
'''

