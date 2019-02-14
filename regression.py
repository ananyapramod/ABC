import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#import data
minedata=pd.read_csv("C:\\Users\\canara\\Documents\\MineData.csv")
airdata=pd.read_csv("C:\\Users\\canara\\Documents\\air quality dataset sample.csv ")
waterdata=pd.read_csv("C:\\Users\\canara\\Documents\\Surface Water Quality Analysis.csv")
noisedata=pd.read_csv("C:\\Users\\canara\\Documents\\noisedata.csv")

#air prediction
airval=airdata.columns.values
airthreshold=airdata['PM10'].quantile(0.90) + airdata['PM2.5'].quantile(0.90)+airdata['NO2'].quantile(0.90) + airdata['O3'].quantile(0.90)+airdata['CO'].quantile(0.90) +airdata['SO2'].quantile(0.90) +airdata['NH3'].quantile(0.90)+airdata['Pb'].quantile(0.90)
airindex=airdata['PM10']/500+airdata['PM2.5']/500 +airdata['NO2']/500 + airdata['O3']/1000+airdata['CO']/50 +airdata['SO2']/2000 +airdata['NH3']/2000+airdata['Pb']/50
airindex=airindex*1000/8

indexvalue=airdata['PM10']/500+airdata['PM2.5']/500 +airdata['NO2']/500 + airdata['O3']/1000+airdata['CO']/50 +airdata['SO2']/2000 +airdata['NH3']/2000+airdata['Pb']/50
indexvalue=indexvalue*1000/8

a=airdata[['Time','Location']]
airindex=pd.concat([a,indexvalue],axis=1)
airindex.columns=["Time","Location","Air Quality Index"]
#print("Enter the location to predict for:")
i='B'
#i="B"
#print(i)
data=airindex.copy().loc[airindex['Location']==i]


X=pd.DataFrame([i for i in range(1,len(data)+1)])
Y=data['Air Quality Index'].reset_index(drop=True)

Z=pd.concat([X,Y],axis=1)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.500)
model=LinearRegression().fit(X_train,Y_train)

#accuracy=Y_test-x
#accuracy=[i*i for i in accuracy]
#accuracy=[i/(len(x)) for i in accuracy]
#print("The  predicted accuracy is ")
#print(sum(accuracy)/len(accuracy))

#print("The predicted values is")
#print(x)
#print("The test values is")
#print(Y_test)
x=model.predict([[len(data)+1]])
print("The air quality index for location " + str(i) +" will be predicted to be "+ str(x[0]))



#water
waterval=waterdata.columns.values
waterthreshold=waterdata['pH'].quantile(0.90) + waterdata['BOD'].quantile(0.90)
waterindex=waterdata['pH']/10+waterdata['BOD']/10
waterindex=waterindex*10/2



a=waterdata[['Date','Location']]
waterindex=pd.concat([a,waterindex],axis=1)
waterindex.columns=["Date","Location","Water Quality Index"]

#print("Enter the location to predict for:")
#i=input()
#i="B"
#print(i)
data=waterindex.copy().loc[waterindex['Location']==i]


X=pd.DataFrame([i for i in range(1,len(data)+1)])
Y=data['Water Quality Index'].reset_index(drop=True)
Z=pd.concat([X,Y],axis=1)
model=LinearRegression().fit(X,Y)
x=model.predict([[6]])
print("The water quality index for location " + str(i) +" will be predicted to be "+str(x[0]))


#noise data
noiseval=noisedata.columns.values
noisethreshold=noisedata['Decibel-Day'].quantile(0.90) + noisedata['Decibel-Night'].quantile(0.90)
noiseindex=noisedata['Decibel-Day']/10+noisedata['Decibel-Night']/10
noiseindex=noiseindex*10/2
noisethreshold=noisethreshold*10/2


a=noisedata[['Time','Location']]
noiseindex=pd.concat([a,noiseindex],axis=1)
noiseindex.columns=["Time","Location","Noise Index"]

#print("Enter the location to predict for:")
#i=input()
#i="B"
#print(i)
data=noiseindex.copy().loc[noiseindex['Location']==i]


X=pd.DataFrame([i for i in range(1,len(data)+1)])
Y=data['Noise Index'].reset_index(drop=True)
Z=pd.concat([X,Y],axis=1)
model=LinearRegression().fit(X,Y)
x=model.predict([[6]])
print("The noise quality index for location " + str(i) +" will be predicted to be "+str(x[0]))

