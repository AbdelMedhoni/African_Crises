from nombreNegatives import *
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import random
from enc import *
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import string
letres = string.ascii_letters
sybmboles = string.punctuation


dataPath = 'african_crises.csv'

data =pd.read_csv(dataPath)

#GENERALIST VISUALISATION


def usd_exch_country(c):
    sns.lineplot(data[data.country==c]['year'],
    data[data.country==c]['exch_usd'],
    label=c,
    color="#6D4C41"
    )
    plt.scatter(data[data.country==c]['year'],
    data[data.country==c]['exch_usd'],
    color="#C0CA33",
    s=30
    )
    plt.plot([np.min(data[np.logical_and(data.country==c,data.independence==1)]['year']),
              np.min(data[np.logical_and(data.country==c,data.independence==1)]['year'])],
             [0,
              np.max(data[data.country==c]['exch_usd'])],
             color='black',
             linestyle='dotted',
             alpha=0.8)
    
    plt.title(c)
    plt.show()




def debt_per_country():
    cols=['systemic_crisis','domestic_debt_in_default','sovereign_external_debt_default','currency_crises','inflation_crises','banking_crisis']
    plt.figure(figsize=(20,20))
    count=1
    for col in cols:
        plt.subplot(3,2,count)
        count+=1
        sns.countplot(y=data.country,hue=data[col],palette='hls')
        plt.legend(loc=0)
        plt.title(col)
    plt.tight_layout()
    plt.savefig("debt_per_country")
    plt.show()
debt_per_country()
#CORROLATION MATRIX AS A HEATMAP
'''sns.heatmap(data.corr()) 

plt.show()'''


#DATA PREPROCESSING
'''Why are we dropping these 3 cols?
1 - banking_crisis: IT is a categorical value and a prediction target.

2 - cc3 : Redunant cause the country's column is sufficient.

3 - gdp_weighted_default : Unreliable (since all values equal 0)
'''
x = data.drop(['banking_crisis','cc3','gdp_weighted_default'],axis=1)

# As mentionned earlier the banking crisis shall be our target column 

y = data.iloc[:,13]
def countingCrisis(): #This function shows the count of both presence and absence of crises.
    sns.countplot(x=y,data=data,palette='hls')
    plt.show()


def banCrisis(): #This function's role is to display the frequency of banking crises on each country
    pd.crosstab(x.country,y).plot(kind='bar') #The line is unreliable cause some countries end up not showing
    plt.show()
def yearCrisis():
    pd.crosstab(x.country,y).plot(kind='bar') #The line is unreliable cause some countries end up not showing
    plt.show()

'''IN ORDER To handle our data we shall replace the crisis no_crisis values in banking crisis
    to 0 and 1's
'''
le=LabelEncoder()
x['country'] = le.fit_transform(x['country']) #OUR COUNTRIES WOULD BE LABELLLED FROM 0 TO 13
y = le.fit_transform(y) #SAME GOES TO CRISIS NO_CRISIS values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1000,random_state=0)
#print(y_test)

#LOGISISTIC REGRESSION

lr = LogisticRegression()

lr.fit(x_train,y_train)
#predLR = lr.predict(x_test)

'''for i in predLR:
    if(predLR[i]==1):
        result.append("crisis")
    else:
        result.append("no_crisis")
for i in range(10):    
    print(result[i])
print("Precision: ",accuracy_score(y_test,predLR))
'''
#KNN ALGORITHM

knn = KNeighborsClassifier()

knn.fit(x_train,y_train)
prKNN = knn.predict(x_test)

print(prKNN)

print("precision: ",accuracy_score(y_test,prKNN))










