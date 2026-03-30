import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Streamlit App")

np.random.seed(42)

df = pd.DataFrame({
    "income": np.random.normal(60000, 15000, 200),
    "spend_score": np.random.randint(1, 100, 200),
    "gender": np.random.choice(["Male", "Female"], 200)
})

gender = st.selectbox("Select Gender", ["All"] + list(df["gender"].unique()))

if gender != "All":
    df = df[df["gender"] == gender]

fig = px.scatter(df, x="income", y="spend_score", color="gender")
st.plotly_chart(fig)

st.dataframe(df)
