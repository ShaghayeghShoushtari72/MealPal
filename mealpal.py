import pandas as pd
import numpy as np
 
# Load the dataset (replace 'data.csv')
df = pd.read_csv('data.csv')
# or:
#import requests
#from bs4 import BeautifulSoup
#import re
#url = "https://mealpal.com/faq/"
#response = requests.get(url)
 
# Convert 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])
 
# Filter data for the last 6-12 months
end_date = pd.to_datetime('today')
start_date = end_date - pd.DateOffset(months=12)
 
filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
 
# Customer Retention Rate
total_customers_at_start = filtered_data[filtered_data['date'] == start_date]['customer_id'].nunique()
total_customers_at_end = filtered_data[filtered_data['date'] == end_date]['customer_id'].nunique()
retention_rate = (total_customers_at_end / total_customers_at_start) * 100
 
# Average User Lifetime Value (LTV)
total_revenue = filtered_data['purchase_amount'].sum()
total_customers = filtered_data['customer_id'].nunique()
ltv = total_revenue / total_customers
 
# Average Order Value
average_order_value = filtered_data['purchase_amount'].mean()
 
print("Customer Retention Rate:", retention_rate)
print("Average User Lifetime Value (LTV):", ltv)
print("Average Order Value:", average_order_value)
