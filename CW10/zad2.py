import pandas as pd
import numpy as np

# Data from the image
data = {
    'Network': ['Aldi', 'Auchan', 'Biedronka', 'Carrefour', 'Carrefour', 'Dino', 'E.Leclerc', 'Intermarche', 'Kaufland', 'Lewiatan', 'Lidl', 'Netto', 'Polo Market', 'SPAR', 'Stokrotka', 'Żabka'],
    'Gorny Slask': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99],
    'Bydgoszcz': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99],
    'Lublin': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99],
    'Warszawa': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99],
    'Trojmiasto': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99],
    'Krakow': [5.99, 4.78, 8.47, 8.85, 12.99, 6.49, 8.99, 6.99, 8.47, 8.47, 5.99, 8.47, 7.99, 7.79, 7.99, 8.99]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Reshape the DataFrame to have 'Network', 'City', and 'Price' columns
df_melted = df.melt(id_vars=['Network'], var_name='City', value_name='Price')

# Calculate the average price of all eggs
average_price = df_melted['Price'].mean()
print(f"Average price of all eggs: {average_price:.2f}")

# Find the cheapest and most expensive eggs by city and network
cheapest = df_melted.loc[df_melted.groupby('City')['Price'].idxmin()][['City', 'Network']]
most_expensive = df_melted.loc[df_melted.groupby('City')['Price'].idxmax()][['City', 'Network']]

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


