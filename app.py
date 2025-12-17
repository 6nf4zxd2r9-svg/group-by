import streamlit as st
import pandas as pd

st.title("Sales Summary by Region")

# Create DataFrame
df = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'South', 'East'],
    'Sales': [100, 150, 200, 180, 120],
    'Orders': [5, 8, 10, 7, 6]
})

st.subheader("Original Data")
st.dataframe(df)

# Total sales by region
total = df.groupby('Region')['Sales'].sum()

st.subheader("Total Sales by Region")
st.dataframe(total)

# Average sales by region
avg = df.groupby('Region')['Sales'].mean()

st.subheader("Average Sales by Region")
st.dataframe(avg)

# Summary statistics
summary = df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Orders': 'sum'
})

st.subheader("Sales & Orders Summary")
st.dataframe(summary)

# Reset index result
result = df.groupby('Region')['Sales'].sum().reset_index()

st.subheader("Final Result (Reset Index)")
st.dataframe(result)
