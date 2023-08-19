import pandas as pd

# Load the cleaned data
sales_data_clean = pd.read_csv('sales_data_clean.csv')

# Remove the dollar signs and commas, and convert 'SALES' and 'PRICEEACH' to numeric
sales_data_clean['SALES'] = sales_data_clean['SALES'].replace({'\$': '', ',': ''}, regex=True).astype(float)
sales_data_clean['PRICEEACH'] = sales_data_clean['PRICEEACH'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Convert 'ORDERDATE' to datetime
sales_data_clean['ORDERDATE'] = pd.to_datetime(sales_data_clean['ORDERDATE'])

# Save the cleaned and transformed data to a new CSV file
sales_data_clean.to_csv('sales_data_clean_transformed.csv', index=False)
