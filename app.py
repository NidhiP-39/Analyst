import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Smart Data Analytics & Prediction System")

df = pd.read_csv("dataset.csv")
st.subheader("Sample Data")
st.write(df.head())

st.subheader("Temperature Trend")
st.line_chart(df["Temperature"])

X = df.index.values.reshape(-1, 1)
y = df["Energy_Usage"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[len(df)+10]])

st.subheader("Prediction")
st.success(f"Predicted future energy usage: {int(prediction[0])} units")
