import streamlit as st
import numpy as np
import pandas as pd

st.title("Retail Transaction Data Dashboard")
st.write(
    "Here is Data Analysis Dashboard from Retail-Transaction dataset. This dataset consist of 30000 entries with 13 column"
)
df = pd.read_csv("Retail_Transactions_Dataset.csv")
st.write("Basic ")
st.write(df)
