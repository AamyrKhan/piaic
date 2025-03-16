import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

url = 'https://raw.githubusercontent.com/AamyrKhan/piaic/refs/heads/main/Sample_Data_for_Plotting_and_Filtering.csv'
df = pd.read_csv(url, index_col=0)

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Data Summary")
st.write(df.describe())

st.subheader("Filter Data")
columns = df.columns.tolist()
selected_column = st.selectbox("Select column to filter by", columns)
unique_values = df[selected_column].unique()
selected_value = st.selectbox("Select value", unique_values)

filtered_df = df[df[selected_column] == selected_value]
st.write(filtered_df)

st.subheader("Plot Data")
x_column = st.selectbox("Select x-axis column", columns)
y_column = st.selectbox("Select y-axis column", columns)

if st.button("Generate Plot"):
    st.line_chart(filtered_df.set_index(x_column)[y_column])
