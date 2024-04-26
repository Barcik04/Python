import numpy as np
import pandas as pd

# Create a numpy array and fix the typo in the data
araj = np.array([[1, 2, 4, 5], [-3, 8, 0.5, 10], [2, -5, 7, 3]])

# Create a DataFrame from the numpy array with custom row labels and column labels
Tablica = pd.DataFrame(araj, index=[f'Row{i}' for i in range(1, 4)], columns=list('ABCD'))

# Display the DataFrame
print("Original DataFrame:")
print(Tablica)

# Example Operations

# Extracting elements
# Accessing a single value by row and column label
value = Tablica.at['Row2', 'C']
print("\nValue at Row2, Column C:", value)

# Accessing a sub-DataFrame
sub_df = Tablica.loc['Row1':'Row2', 'B':'C']
print("\nSub-DataFrame from Row1 to Row2 and Column B to C:")
print(sub_df)

# Sorting by a column
# Sorting the DataFrame by values in column 'B'
sorted_df = Tablica.sort_values(by='B', ascending=False)
print("\nDataFrame sorted by column B:")
print(sorted_df)

# Changing shape
# Transpose the DataFrame
transposed_df = Tablica.T
print("\nTransposed DataFrame:")
print(transposed_df)
