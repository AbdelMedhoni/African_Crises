import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import random



dataPath = 'african_crises.csv'

data =pd.read_csv(dataPath)

unique_countries=data.country.unique()

def exch_usd_avg():
    sns.set(style='whitegrid')
    plt.figure(figsize=(20,20))
    count=1
    for country in unique_countries:
        plt.subplot(5,3,count)
        count+=1
        col="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        sns.lineplot(data[data.country==country]['year'],
                 data[data.country==country]['exch_usd'],
                 label=country,
                 color=col)
        plt.scatter(data[data.country==country]['year'],
                data[data.country==country]['exch_usd'],
                color=col,
                s=28)
        plt.plot([np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
              np.min(data[np.logical_and(data.country==country,data.independence==1)]['year'])],
             [0,
              np.max(data[data.country==country]['exch_usd'])],
             color='black',
             linestyle='dotted',
             alpha=0.8)
        plt.text(np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
             np.max(data[data.country==country]['exch_usd'])/2,
             'Independence',
             rotation=-90)
        plt.scatter(x=np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
                y=0,
                s=50)
        plt.title(country)
    plt.tight_layout()
    plt.show()

def debt_diff():
    sns.set(style='darkgrid')
    cols=['systemic_crisis','domestic_debt_in_default','sovereign_external_debt_default','currency_crises','inflation_crises','banking_crisis']
    plt.figure(figsize=(20,20))
    count=1
    for col in cols:
        plt.subplot(3,2,count)
        count+=1
        sns.countplot(y=data.country,hue=data[col],palette='rocket')
        plt.legend(loc=0)
        plt.title(col)
    plt.tight_layout()
    plt.show()

def inflation_avg():
    sns.set(style='whitegrid')
    plt.figure(figsize=(20,20))
    count=1
    for country in unique_countries:
        plt.subplot(5,3,count)
        count+=1
        col="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        sns.lineplot(data[data.country==country]['year'],
                 data[data.country==country]['inflation_annual_cpi'],
                 label=country,
                 color=col)
        plt.scatter(data[data.country==country]['year'],
                data[data.country==country]['inflation_annual_cpi'],
                color=col,
                s=28)
        plt.plot([np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
              np.min(data[np.logical_and(data.country==country,data.independence==1)]['year'])],
             [np.min(data[data.country==country]['inflation_annual_cpi']),
              np.max(data[data.country==country]['inflation_annual_cpi'])],
             color='black',
             linestyle='dotted',
             alpha=0.8)
        plt.text(np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
             np.max(data[data.country==country]['inflation_annual_cpi'])/2,
             'Independence',
             rotation=-90)
        plt.scatter(x=np.min(data[np.logical_and(data.country==country,data.independence==1)]['year']),
                y=np.min(data[data.country==country]['inflation_annual_cpi']),
                s=50)
    plt.title(country)
    plt.tight_layout()
    plt.show()

inflation_avg()
