import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / 'data' / 'processed' / 'retail_cleaned.csv'
OUT = ROOT / 'outputs'

st.set_page_config(page_title='AI Retail BI Platform', layout='wide')
st.title('AI-Powered Retail Business Intelligence Platform')
st.caption('Sales analytics, customer segmentation, fraud detection, recommendations and business KPIs')

if not DATA.exists():
    st.warning('Please run: python generate_data.py and python run_pipeline.py first')
    st.stop()

df = pd.read_csv(DATA)
df['order_date'] = pd.to_datetime(df['order_date'])

with st.sidebar:
    st.header('Filters')
    city = st.multiselect('City', sorted(df['city'].dropna().unique()), default=sorted(df['city'].dropna().unique()))
    category = st.multiselect('Category', sorted(df['category'].dropna().unique()), default=sorted(df['category'].dropna().unique()))
    year = st.multiselect('Year', sorted(df['year'].dropna().unique()), default=sorted(df['year'].dropna().unique()))

filtered = df[df['city'].isin(city) & df['category'].isin(category) & df['year'].isin(year)]

c1, c2, c3, c4 = st.columns(4)
c1.metric('Revenue', f"₹{filtered['revenue'].sum():,.0f}")
c2.metric('Profit', f"₹{filtered['profit'].sum():,.0f}")
c3.metric('Orders', f"{filtered['order_id'].nunique():,}")
c4.metric('Customers', f"{filtered['customer_id'].nunique():,}")

st.subheader('Revenue Trend')
monthly = filtered.groupby('month', as_index=False)['revenue'].sum()
st.plotly_chart(px.line(monthly, x='month', y='revenue', markers=True), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader('Revenue by Category')
    cat = filtered.groupby('category', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
    st.plotly_chart(px.bar(cat, x='category', y='revenue'), use_container_width=True)
with col2:
    st.subheader('Revenue by City')
    city_df = filtered.groupby('city', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)
    st.plotly_chart(px.bar(city_df, x='city', y='revenue'), use_container_width=True)

st.subheader('Top Products')
top_products = filtered.groupby('product_name', as_index=False).agg(revenue=('revenue','sum'), profit=('profit','sum'), orders=('order_id','count')).sort_values('revenue', ascending=False).head(10)
st.dataframe(top_products, use_container_width=True)

st.subheader('Customer Segmentation')
seg_file = OUT / 'customer_segments.csv'
if seg_file.exists():
    seg = pd.read_csv(seg_file)
    st.plotly_chart(px.scatter(seg, x='frequency', y='monetary', color='segment_name', size='monetary', hover_data=['customer_id','recency']), use_container_width=True)
else:
    st.info('Run pipeline to generate customer segments.')

st.subheader('Fraud Detection Alerts')
fraud_file = OUT / 'fraud_alerts.csv'
if fraud_file.exists():
    fraud = pd.read_csv(fraud_file)
    st.dataframe(fraud[fraud['fraud_status']=='Suspicious'].head(30), use_container_width=True)

st.subheader('Product Recommendations')
rec_file = OUT / 'product_recommendations.csv'
if rec_file.exists():
    recs = pd.read_csv(rec_file)
    selected_product = st.selectbox('Select product', recs['product_name'])
    st.success(recs.loc[recs['product_name']==selected_product, 'recommended_products'].iloc[0])

st.subheader('Business Summary')
summary_file = OUT / 'business_summary.csv'
if summary_file.exists():
    st.dataframe(pd.read_csv(summary_file), use_container_width=True)
