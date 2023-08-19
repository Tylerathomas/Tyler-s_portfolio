import pandas as pd

# Load the original data with the correct encoding
sales_data = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')

# Drop 'ADDRESSLINE2'
sales_data_clean = sales_data.drop(columns='ADDRESSLINE2')

# Fill missing 'STATE' values with 'N/A'
sales_data_clean['STATE'].fillna('N/A', inplace=True)

# Format 'PRICEEACH' and 'SALES' to dollar format
sales_data_clean['PRICEEACH'] = sales_data_clean['PRICEEACH'].map('${:,.2f}'.format)
sales_data_clean['SALES'] = sales_data_clean['SALES'].map('${:,.2f}'.format)

# Save the cleaned data to a new CSV file
sales_data_clean.to_csv('sales_data_clean.csv', index=False)
