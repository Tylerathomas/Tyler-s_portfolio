import pandas as pd

# Load the original data
data = pd.read_csv('/mnt/data/gamesovertime.csv')

# Convert 'Release Date' to datetime format
data['Release Date'] = pd.to_datetime(data['Release Date'])

# Convert 'Rating' to numeric
data['Rating'] = pd.to_numeric(data['Rating'])

# Convert 'Number of Reviews', 'Plays', 'Playing', 'Backlogs', 'Wishlist' to numeric by removing 'K' and converting to thousands
columns_to_convert = ['Number of Reviews', 'Plays', 'Playing', 'Backlogs', 'Wishlist']
for column in columns_to_convert:
    data[column] = data[column].str.replace('K', '').astype(float) * 1000

# Remove 'Times Listed' column
data = data.drop(columns=['Times Listed'])

# Remove rows with "Release Date" as "releases on TBD"
data = data[data['Release Date'] != 'releases on TBD']
data['Release Date'] = pd.to_datetime(data['Release Date'])

# Parse 'Team' and 'Genres' columns
data['Team'] = data['Team'].str.replace('[','').str.replace(']','').str.replace("'",'').str.split(',')
data['Genres'] = data['Genres'].str.replace('[','').str.replace(']','').str.replace("'",'').str.split(',')

# Save the cleaned data to a new CSV file
data.to_csv('/mnt/data/cleaned_gamesovertime.csv', index=False)
