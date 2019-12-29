import string
letres = string.ascii_letters
sybmboles = string.punctuation
import random
import re

def changeIt(f): 
    cStr = " "
    if(f<0):
        if(type(f)==float):
            t = str(f)
            t = t[1:]
            f = float(t)
            cStr = cStr + '-'
        if(type(f)==int):
            t = str(f)
            t = t[1:]
            f = int(t)
            cStr = cStr + '-'
        
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
        if(f<0):
            return "-" + cStr
        return  cStr 



def getItBack(f):
    og = ' '
    if (f=="rien"):
        og = "0"
        return og
    
    if(',' in f):
        if(f[1]=='-'):
        
            f = f[2:]
            og = og + '-'
        f = f.replace("Point","@")
        f = f.replace("rien","=")
        ls = f.split(",")
        ls = list(filter(None,ls))
        
        
        
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
    else:
        og = str(len(f))       
        
    return float(og)

def getItBackInt(f):
    ok = ' '
    og = 0
    if(f=="rien"):
        return 0
    if(f[1]=='-'):
        ok = ok + '-'
        
        f = f[2:]
    for i in range(0,len(f)):
        if(f[i]in letres):
            og = og + 1
    ok = ok + str(og)
    return int(ok)

