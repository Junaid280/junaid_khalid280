import streamlit as st
import seaborn as sns
st.header("Hello World")
st.text("This is a test")
df=sns.load_dataset("iris")
st.write(df[['sepal_length','sepal_width']].head(10))
# st.bar_chart(df[['sepal_length','sepal_width']])
st.bar_chart(df)
st.line_chart(df)
st.line_chart(df[['sepal_length','sepal_width']])