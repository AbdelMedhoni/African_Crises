import string
letres = string.ascii_letters
sybmboles = string.punctuation
import random
import re

def changeIt(f):    
    cStr = ""
    if (type(f)== int and (f == 0 )):
        return "rien"
    if (type(f) is int):
        for i in range(0,f):
            cStr = cStr + random.choice(letres)
        return cStr 
    if(type(f) is float):
        stringToCode = str(f)
        for i in range(0,len(stringToCode)):
            if(stringToCode[i]=='0'):
                cStr = cStr+ "rien" + ','
            if (stringToCode[i] == "."):
                cStr = cStr + "Point" + ','
            else:
                for j in range(0,int(stringToCode[i])):
                    cStr = cStr + random.choice(letres)
                cStr = cStr + ','
        return  cStr 



def getItBack(f):
    f = f.replace("Point","@")
    f = f.replace("rien","=")
    ls = f.split(",")
    ls = list(filter(None,ls))
    print(ls)
    og = ' '
    f = f + '-'
    c = ' '
    i = 0
    compt = 0
    for el in ls:
                          
        if(len(el)==1):
            
            if(el[0]=='='):
                og = og + '0'
                
            if(el[0]=='@'):
                og = og + '.'
                
            if(el[0]in letres):
                og = og + '1'
                
        if(len(el)>1):
            og = og + str(len(el))    
            
        
    return og


f = changeIt(81.1)

