import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="E-Commerce Sales Dashboard", layout="wide")

st.title("E-Commerce Sales Dashboard")


df = pd.read_csv("C:/Users/hp/Desktop/Python/Projects/Sales/Amazon Sale Report.csv/Amazon Sale Report.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_')


df = df.dropna(subset=['amount', 'category', 'ship_state'])


category_sales = df.groupby('category')['amount'].sum().reset_index().sort_values(by='amount', ascending=False)
fig_cat = px.bar(category_sales,
                 x='category',
                 y='amount',
                 title='Total Sales by Category',
                 labels={'amount': 'Sales (INR)', 'category': 'Product Category'},
                 color='amount',
                 text_auto=True)


state_sales = df.groupby('ship_state')['amount'].sum().reset_index().sort_values(by='amount', ascending=False)
fig_state = px.bar(state_sales,
                   x='amount',
                   y='ship_state',
                   orientation='h',
                   title='Total Sales by State',
                   labels={'amount': 'Sales (INR)', 'ship_state': 'State'},
                   color='amount',
                   text_auto=True)


col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_cat, use_container_width=True)

with col2:
    st.plotly_chart(fig_state, use_container_width=True)