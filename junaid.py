
import pandas as pd   
import plotly.express as px
import streamlit as st
import seaborn as sns  
df=sns.load_dataset('iris')
st.title("iris dataset")
st.write(df)
st.write(df.columns)
st.write(df.describe())


