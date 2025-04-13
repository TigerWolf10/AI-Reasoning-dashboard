import streamlit as st
import pandas as pd
from supabase_client import supabase

st.set_page_config(page_title="Supabase Reasoning App", layout="wide")
st.title("Sales Reasoning Dashboard")

@st.cache_data
def get_data():
    result = supabase.table("transactions").select("*").execute()
    return pd.DataFrame(result.data)

df = get_data()

st.subheader("1. Supabase Data")
st.dataframe(df)

st.subheader("2. o1 Reasoning Queries")
o1_queries = {
    "What products did Alice purchase?": lambda df: df[df["CustomerName"] == "Alice"]["ProductName"].unique().tolist(),
    "Which category does 'Desk' belong to?": lambda df: df[df["ProductName"] == "Desk"]["Category"].unique().tolist(),
    "Which region does Bob live in?": lambda df: df[df["CustomerName"] == "Bob"]["Region"].unique().tolist(),
    "What was the sales amount of transaction T002?": lambda df: df[df["TransactionID"] == "T002"]["SalesAmount"].values.tolist()
}

selected_o1 = st.selectbox("Choose an o1 query", list(o1_queries.keys()))
if st.button("Run o1 Query"):
    result = o1_queries[selected_o1](df)
    st.write("Result:", result)

st.subheader("3. o3 Reasoning Queries")
o3_queries = {
    "Which categories has Alice purchased from?": lambda df: df[df["CustomerName"] == "Alice"]["Category"].unique().tolist(),
    "Which customers from the West purchased Electronics?": lambda df: df[(df["Region"] == "West") & (df["Category"] == "Electronics")]["CustomerName"].unique().tolist(),
    "Total sales by region for Electronics category": lambda df: df[df["Category"] == "Electronics"].groupby("Region")["SalesAmount"].sum(),
    "Total Furniture sales in South region": lambda df: df[(df["Region"] == "South") & (df["Category"] == "Furniture")]["SalesAmount"].sum()
}

selected_o3 = st.selectbox("Choose an o3 query", list(o3_queries.keys()))
if st.button("Run o3 Query"):
    result = o3_queries[selected_o3](df)
    st.write("Result:", result)
