import pandas as pd
import numpy as np

# Data from the image
data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype=str)

# Convert the data into a DataFrame
columns = data[0]  # First row as column names
rows = data[1:]    # The rest as data

# Create DataFrame
df = pd.DataFrame(rows, columns=columns)

# Convert prices to numeric, handle missing values
df = df.melt(id_vars=[''], var_name='City', value_name='Price')
df.columns = ['Network', 'City', 'Price']
df['Price'] = pd.to_numeric(df['Price'].str.replace(',', '.'), errors='coerce')
print(data)

# Calculate the average price of all eggs
average_price = df['Price'].mean()
print(f"Average price of all eggs: {average_price:.2f}")

# Find the cheapest and most expensive eggs by city and network
cheapest = df.loc[df.groupby('City')['Price'].idxmin()][['City', 'Network', 'Price']]
most_expensive = df.loc[df.groupby('City')['Price'].idxmax()][['City', 'Network', 'Price']]

# Store results in a two-dimensional array using a list of tuples
results_array = np.array([
    ("Cheapest", cheapest.values.tolist()),
    ("Most Expensive", most_expensive.values.tolist())
], dtype=object)

# Print results
print("Cheapest eggs by city and network:")
print(cheapest)
print("\nMost Expensive eggs by city and network:")
print(most_expensive)

# Optionally, to see the array of results
print("\nResults array:")
print(results_array)
