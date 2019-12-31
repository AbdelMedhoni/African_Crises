from afro import *

print("Testing out our functunalities\t")

print("Our chosen country would be Morocco!\n")

usd_exch_country("Morocco")


print("And now we'll get a visual of all crises!\n")


debt_per_country()

countingCrisis()

banCrisis()

yearCrisis()

print("And now for the predictions:\n ")

print("\tLOGISTIC REGRESSION\n")

result = []
for i in predLR:
    if(predLR[i]==1):
        result.append("crisis")
    else:
        result.append("no_crisis")
for i in range(10):    
    print(result[i])
print("Precision: ",accuracy_score(y_test,predLR))


print("\tKNN\n")

resultknn = []
for i in prKNN:
    if(prKNN[i]==1):
        resultknn.append("crisis")
    else:
        resultknn.append("no_crisis")
for i in range(10):    
    print(result[i])
print("Precision: ",accuracy_score(y_test,prKNN))
