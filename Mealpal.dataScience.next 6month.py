import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load customer service tickets data
data = pd.read_csv('customer_service_tickets.csv')

# Define retention based on user activity in the next 6 months using if...else
data['Retention'] = data['activity_in_next_6_months'].apply(lambda x: 1 if x == 'continued' else 0)

# Features for modeling 
features = ['sentiment_score', 'past_order_count', 'ticket_category']

# Prepare features and target variable
X = data[features]
y = data['Retention']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model performance using accuracy score
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Calculate metrics
customer_retention_rate = data['Retention'].mean()

# Calculate average user lifetime value (LTV) and average order value for retained customers
avg_ltv_retained = data[data['Retention'] == 1]['lifetime_value'].mean()
avg_order_value_retained = data[data['Retention'] ==1]['order_value'].mean()

print("Customer Retention Rate:", customer_retention_rate)
print("Average User Lifetime Value (LTV) for Retained Customers:", avg_ltv_retained)
print("Average Order Value for Retained Customers:", avg_order_value_retained)
