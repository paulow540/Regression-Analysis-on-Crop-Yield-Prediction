from sklearn.model_selection import train_test_split  #this help us to split our dataset into training and testing data
from sklearn.tree import DecisionTreeRegressor   #this is use for machine learning model for regression analysis
from sklearn import preprocessing # this is use to pre process our dataset removing outliers and scaling our datset
import sklearn.metrics as metrics # to check for the performance of our model

import pandas as pd  #data importing and cleaning
import numpy as np #multi array demensionality
import math  #for math calculation
import pickle  #is the process whereby a Python object hierarchy is converted into a byte stream
# import seaborn as sns


#This is the function that help to clean and remove unwanted columns in our datate
#we use get_dummies that Convert categorical variable into dummy/indicator variables
def preprocess(df):

    df['Export Quantity'] = df['Export Quantity'].interpolate(method='linear', limit_direction='backward', axis=0)
    scaler = preprocessing.StandardScaler()
    scal_feat = ['Temperature (Avg)','Precipitation','Export Quantity','Fertilizer Usage']
    df[scal_feat]=scaler.fit_transform(df[scal_feat].to_numpy())
    feat = scal_feat + ["Crop"]
    X = df[feat].copy(deep=True)
    X = pd.get_dummies(X, columns = ['Crop'])
    y = df['Yield'].copy(deep=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 13)

    return X_train, X_test, y_train, y_test, X



#this function check for the mean absolute error and the mean_squared_error
def compute_scores(y_test, y_pred):
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse) 
    r2 = metrics.r2_score(y_test, y_pred)
    print("MAE : ",mae)
    print("MSE : ",mse)
    print("RMSE : ",rmse)
    print("R2 : ",r2)


# this is where i load the dataset called crop_yield_data in Data folder with pandas library 
df = pd.read_csv("Data/crop_yield_data.csv")

# i drop the year columns from the dataset 
df = df.drop(columns=["Year"], axis =1 )    


# this is where we map our preprocess function to our train and test for machine learning 
X_train, X_test, y_train, y_test, X = preprocess(df)


#i make use of DecisionTree regresssor for the machine learning algorithm to train, test and predict base on our
#preprocess and data cleaning 
dt_regression = DecisionTreeRegressor()
dt_regression.fit(X_train, y_train)
y_pred_dt = dt_regression.predict(X_test)
compute_scores(y_test, y_pred_dt)

#this is the code that save our predicted values to a model.pkl file
pickle.dump(dt_regression, open("model.pkl","wb"))

