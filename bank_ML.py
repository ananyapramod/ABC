import numpy as np
import pandas as pn
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
#load training data from folder
linktrain="C:\\Users\\canara\\Downloads\\loan-analysis\\train.csv"
datatrain=pn.read_csv(linktrain)
print(type(datatrain))
#transform categorical data into integers
for i in ['Loan_ID','Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']:
    datatrain[i]=LabelEncoder().fit_transform(datatrain[i].astype('str'))

#fill NaN values with 0
datatrain=datatrain.fillna(0)

#datasettrain has no labels
#datasettrain is list of  lists
datasettrain=datatrain.values

#Xtrain contains only feature data
Xtrain=datasettrain[:25,:12]
Xtrain=scale(Xtrain)
#Ytrain contains only the actual y
Ytrain=datasettrain[:25,12]

#split data  into test and training set
xtrain,xtest,ytrain,ytest=model_selection.train_test_split(Xtrain,Ytrain,test_size=0.25)

#to print only the unique elements in a  column
#le=LabelEncoder()
#le.fit(datatrain['Credit_History'])
#print(le.classes_)

#recursive feature elimination-recursively removes attribubtes and builds model on the feature that remain.
#Hence,the model is  built on those features that contribute the most to predicting the output.
rfeprediction=RFE(LogisticRegression(),5)
rfeprediction=rfeprediction.fit(xtrain,ytrain)

rfe=rfeprediction.predict(xtest)
print("The accuracy with feature elimination is")
print(accuracy_score(rfe,ytest))

#logistic regression without feature elimination
abc=LogisticRegression().fit(xtrain,ytrain)
y=abc.predict(xtest)
print("The accuracy without feature eliminaation is ")
print(accuracy_score(ytest,y))

abc=DecisionTreeClassifier().fit(xtrain,ytrain)
xy=abc.predict(xtest)
print("The accuracy using decision tree is ")
print(accuracy_score(ytest,xy))
