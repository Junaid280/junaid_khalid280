import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from PIL import Image
from  sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv('diabetes.csv')
#Headings
st.header("Diabetes Prediction App")
st.sidebar.header("Patient information")
st.subheader("Description of stats ") 
st.write(df.describe())
x=df.drop(['Outcome'],axis=1)
y=df['Outcome']
# splitting data into training and testing data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0) 

# function 
def user_report():
    pregnancies=st.sidebar.slider('Pregnancies',0,17,3)
    glucose=st.sidebar.slider('Glucose',0,199,117)
    bloodpressure=st.sidebar.slider('BloodPressure',0,122,72)
    skinthickness=st.sidebar.slider('SkinThickness',0,99,23)
    insulin=st.sidebar.slider('Insulin',0.0,846.0,30.0)
    bmi=st.sidebar.slider('BMI',0.0,67.1,32.0)
    dpf=st.sidebar.slider('DiabetesPedigreeFunction',0.078,2.42,0.3725)
    age=st.sidebar.slider('Age',21,81,29)
    user_report_data={
        'Pregnancies':pregnancies,
        'Glucose':glucose,
        'BloodPressure':bloodpressure,
        'SkinThickness':skinthickness,
        'Insulin':insulin,
        'BMI':bmi,
        'DiabetesPedigreeFunction':dpf,
        'Age':age}
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data
user_data=user_report()
st.subheader("Patient report")
st.write(user_data)
# Model building and fitting
model=RandomForestClassifier().fit(x_train,y_train)
# prediction 
user_result=model.predict(user_data)
# visualizing the result
st.title("Visualizing the patient  result")
#color function
if user_result[0]==0:
    color='blue'
else:
    color='red'
# age vs pregnancies
st.header("Age vs Pregnancies")
fig_preg=plt.figure()
ax1=sns.scatterplot(x='Age',y='Pregnancies',data=df,hue='Outcome')
ax2=sns.scatterplot(x=user_data["Age"],y=user_data["Pregnancies"],s=150,color=color)
plt.xticks(np.arange(10,85,step=5))
plt.yticks(np.arange(0,17,step=1))
plt.title("0 -- Healthy & 1 -- Diabetic")
st.pyplot(fig_preg)
#out put
st.header("Your Report is ready ")
output=""
if user_result[0]==0:
    output="You are Healthy"
else:
    output="You are Diabetic"
st.title(output)
# accuracy
st.header("Accuracy")
st.write(accuracy_score(y_test,model.predict(x_test)))


