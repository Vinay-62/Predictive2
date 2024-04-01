# -*- coding: utf-8 -*-
"""LVADSUSR131_vinay_I2_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17OQSH39UDk48ZWRniM0LOutRPXzwD01a
"""

#dataset
import pandas as pd
data=pd.read_csv("/content/Mall_Customers.csv")
df=pd.DataFrame(data)
df.head()

#find null values
df.isnull().sum()

#to fill the null values
df = df.fillna(method='ffill')

#models
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])
scaler.fit(df[['Annual Income (k$)']])
df[['Annual Income (k$)']]=scaler.transform(df[['Annual Income (k$)']])
scaler.fit(df[['Spending Score (1-100)']])
df[['Spending Score (1-100)']]=scaler.transform(df[['Spending Score (1-100)']])

le=LabelEncoder()
df['Gender']=le.fit_transform(df['Gender'])
km = KMeans(n_clusters=2)
y_predicted = km.fit_predict(df[['Gender','Age','Annual Income (k$)','Spending Score (1-100)']])
df['cluster']=y_predicted
print(km.cluster_centers_)

#Elbow method
s=[]
k_r = range(1,10)
for k in k_r:
    km = KMeans(n_clusters=k)
    km.fit(df)
    s.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('squared error')
plt.plot(k_r,s)

print(df['cluster'].unique())

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
plt.scatter(df1.Age,df1['Gender'],color='green')
plt.scatter(df2.Age,df2['Gender'],color='red')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Gender')
plt.legend()