# -*- coding: utf-8 -*-
"""Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s4X8gzX7UkEGhZbgs_OaiP3N2N7EmiXY

# Importing Packages
"""

import numpy as np 
import pandas as pd
import seaborn as sns
import pickle


"""# Loading the data"""

df = pd.read_csv(r'C:\Users\megha\University of verona\Programming\Hotel_review\makemytrip.csv',low_memory=False)
df.shape

df.head()

data = df[['area','city','in_your_room','mmt_review_score','hotel_star_rating']]
data.head()
data.tail()


data.describe()
data.info()



# Data Cleaning
# Filling the area and in_your_room using intepolate method

data['area'].interpolate(method='pad',inplace=True)
data['in_your_room'].interpolate(method='pad',inplace=True)
data = data.replace({'hotel_star_rating' : { '1 star' : 1, '2 star' : 2, '3 star' : 3, '4 star' : 4, '5 star' : 5, 'Three on 5' : 3,'Four on 5' : 4,'Five on 5': 5,'Four star': 4 }})

# Considering the target value as it is having more than 50% null values
X = data['mmt_review_score']

x= X.values.reshape(-1,1)

x

"""# Filling null values in target variable"""


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer = imputer.fit(x)

data['mmt_review_score'] = imputer.transform(x)

data.head()

sns.heatmap(data.isnull(),cbar=False,cmap='viridis')
data['hotel_star_rating']=data['hotel_star_rating'].astype('int32') 
data.head()

data['in_your_room'].replace('{{value}}',np.nan, inplace=True)
data.isnull().sum()

data['in_your_room']=data['in_your_room'].astype('str')

#Splitting the data using '/' inorder to count facilities
def function(str):
     return len(str.split('|'))

data["count_in_your_room"]=data.apply(lambda x:function(x["in_your_room"]),axis=1)

data.drop(['in_your_room'], axis=1,inplace=True)
data.drop(['city'], axis=1,inplace=True)
data.head()

#Converting the categorical variables using one-hot encoding
City=pd.get_dummies(df['city'],drop_first=True,dummy_na=False)
df3=pd.DataFrame(City)
df3

from pandas import DataFrame
df1=pd.DataFrame(data[['hotel_star_rating','count_in_your_room']])
df2=pd.DataFrame(data['mmt_review_score'])

#concatinating all the data frames

final = pd.concat([df1,df2], axis=1)
final

#checking the correlation between the columns present in data
data.corr()
data.columns

"""# Outlier detection"""

sns.boxplot(x=final['mmt_review_score'])

sns.boxplot(x=final['count_in_your_room'])

sns.boxplot(x=final['hotel_star_rating'])

Q1 = final.quantile(0.25)
Q3 = final.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

final.shape

x=final.iloc[:,0:2:]
x

y=final.iloc[:,2:3:]
y

y.shape

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=200)

x_train

#DecisionTreeRegModel = DecisionTreeRegressor(criterion='mse',random_state=100,max_depth=10,min_samples_leaf=15)
#DecisionTreeRegModel.fit(x_train,y_train)

#y_pred = DecisionTreeRegModel.predict(x_test)

#y_pred

"""# Random Forest Algorithm"""

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor()

regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

max_features=['sqrt','log2']
min_samples_split=[3,5]
min_samples_leaf=[2,5]

param={'max_features':max_features,'min_samples_split':min_samples_split,'min_samples_leaf':min_samples_leaf}

#rfr_random=RandomizedSearchCV(estimator=rfr,param_distributions=param,n_iter=500,cv=5,verbose=2,random_state=42,n_jobs=-1)

from sklearn.model_selection import RandomizedSearchCV
rfr=RandomForestRegressor(random_state=1)
rfr_random=RandomizedSearchCV(estimator=rfr,param_distributions=param,n_iter=500,cv=5,verbose=2,random_state=42,n_jobs=-1)

rfr_random.fit(x_train,y_train)

print(rfr_random.best_params_)

"""# RMSE Score"""

mse= mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
rmse

regressor.predict([[2,3]])

"""# Loading onto pickle file"""

#from sklearn.externals import joblib

#import joblib

#joblib.dump('regressor', open('a.pkl','wb'))

#model = joblib.load(open('a.pkl','rb'))

pickle.dump(regressor, open('final.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('final.pkl','rb'))

print(model.predict([[2,3]]))

