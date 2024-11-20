import streamlit as st
import numpy as np
import pandas as pd

st.title("Retail Transaction Data Dashboard")
st.write(
    "Here is Data Analysis Dashboard from Retail-Transaction dataset. This dataset consist of 30000 entries with 13 column"
)
df = pd.read_csv("Retail_Transactions_Dataset.csv")
st.write("Here is a quick view on the data: ")
st.write(df)
st.write("To view 10 most popular items being purchased ")
df_item_perseason = df.groupby("Season")["Product"]

Most_Purchased=df["Product"].explode().value_counts().head(10)
Most_winter = df_item_perseason.get_group("Winter").explode().value_counts().head(10)
Most_summer = df_item_perseason.get_group("Summer").explode().value_counts().head(10)
Most_Fall = df_item_perseason.get_group("Fall").explode().value_counts().head(10)
Most_Spring = df_item_perseason.get_group("Spring").explode().value_counts().head(10)

option_season=st.selectbox("Choose Seasons",["All times","Spring","Summer","Fall","Winter"])
if option_season=="All times":
    st.bar_chart(Most_Purchased, x_label="Product",y_label="Amount")
elif option_season=="Winter":
    st.bar_chart(Most_winter, x_label="Product",y_label="Amount")
elif option_season=="Summer":
    st.bar_chart(Most_summer, x_label="Product",y_label="Amount")
elif option_season=="Spring":
    st.bar_chart(Most_Spring, x_label="Product",y_label="Amount")
else :
    st.bar_chart(Most_Fall, x_label="Product",y_label="Amount")