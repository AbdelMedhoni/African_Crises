from nombreNegatives import *
import pandas as pd 
import matplotlib.pyplot as plt
import string
letres = string.ascii_letters
sybmboles = string.punctuation


dataPath = 'african_crises.csv'

data =pd.read_csv(dataPath)



def encrypt(tab):
    lines,columns = tab.shape
    for i in range (0,lines):
        for j in range (0,columns):
        
            if(j==5):
                continue
            if(type(tab[i][j])==int):
                tab[i][j] = changeIt(tab[i][j])
            if (type(tab[i][j])==float):
                tab[i][j] = changeIt(tab[i][j])
    return tab




#print(newData.head())
def decrypt(tab):
    lines,columns = tab.shape
    for i in range (0,lines):
        for j in range (0,columns):
        
            if(j==1 or j==2  or j==5 or j==13):
                continue
            if(","in tab[i][j]):         
                tab[i][j] = getItBack(tab[i][j])
            else:
                tab[i][j] = getItBackInt(tab[i][j])
    return tab


def dfToNumpy(df):
    tab = data.to_numpy()
    return tab


def tabToDF(tab):
    newData = pd.DataFrame(data=tab,columns=data.columns.values)
    return newData

newD = (tabToDF(decrypt(encrypt(dfToNumpy(data)))))

cs = newD.to_csv(r'C:\Users\Abderrahman\Desktop\Projects and stuff\PFM_Python\CRYPTED.csv')
