import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# App Title
st.title("Smart Data Analytics & Prediction System")
st.write("Upload a CSV file to analyze data and make predictions")

# CSV Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset (Preview)")
    st.write(df.head())

    # Select numeric columns only
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if len(numeric_columns) < 2:
        st.error("The dataset must contain at least TWO numeric columns.")
    else:
        # Column selection
        x_col = st.selectbox("Select Independent Variable (X)", numeric_columns)
        y_col = st.selectbox("Select Dependent Variable (Y)", numeric_columns)

        # Visualization
        st.subheader(f"{y_col} Trend")
        st.line_chart(df[y_col])

        # Machine Learning Model
        X = df[x_col].values.reshape(-1, 1)
        y = df[y_col].values

        model = LinearRegression()
        model.fit(X, y)

        # Prediction
        next_value = [[X[-1][0] + 1]]
        prediction = model.predict(next_value)

        st.subheader("Prediction Result")
        st.success(f"Predicted next value of {y_col}: {prediction[0]:.2f}")

else:
    st.info("Please upload a CSV file to continue.")
