import numpy as np
import pandas as pd

# Read the sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')

# Convert the revenue column to numeric (remove $ sign if present)
sales_data['Revenue'] = sales_data['Revenue'].replace('[\$,]', '', regex=True).astype(float)

# 1. Total revenue generated during the period
total_revenue = np.sum(sales_data['Revenue'])

# 2. Average quantity sold per sale
average_quantity = np.mean(sales_data['Quantity'])

# 3. Maximum and minimum revenue generated in a single sale
max_revenue = np.max(sales_data['Revenue'])
min_revenue = np.min(sales_data['Revenue'])

# 4. Total revenue generated for each product
total_revenue_per_product = sales_data.groupby('Product')['Revenue'].sum()

# 5. Total revenue generated for each month
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Month'] = sales_data['Date'].dt.month_name()
total_revenue_per_month = sales_data.groupby('Month')['Revenue'].sum()

# Print the results
print("Total revenue generated during the period: ${:.2f}".format(total_revenue))
print("Average quantity sold per sale: {:.1f}".format(average_quantity))
print("Maximum revenue generated in a single sale: ${:.2f}".format(max_revenue))
print("Minimum revenue generated in a single sale: ${:.2f}".format(min_revenue))
print("Total revenue generated for each product:")
print(total_revenue_per_product)
print("Total revenue generated for each month:")
print(total_revenue_per_month)
