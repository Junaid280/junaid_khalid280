import streamlit as st
import pandas as pd
import joblib
from PIL import Image
#Loading Our final trained Knn model 
model= open("Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)
st.title("Iris flower species Classification App")
#Loading images
setosa= Image.open('setosa.png')
versicolor= Image.open('versicolor.png')
virginica = Image.open('virginica.png')

st.sidebar.title("Features")
#Intializing
parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']
values=[]

if st.button("Click Here to Classify"):
 prediction = knn_clf.predict(input_variables)
st.image(setosa) if prediction == 0 else st.image(versicolor)  if prediction == 1 else st.image(virginica)


 
