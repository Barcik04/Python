import numpy as np
import pandas as pd

# Initial data structures
my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
my_series = pd.Series([1, 32, -37, 91, 12, 11, -5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Converting list to DataFrame
list_df = pd.DataFrame([my_list], index=['Row1'], columns=[f'Col{i}' for i in range(1, len(my_list) + 1)])
print("List as DataFrame:")
print(list_df)

# Converting array to DataFrame
array_df = pd.DataFrame(my_array, index=[f'Row{i}' for i in range(1, 4)], columns=[f'Column{i}' for i in range(1, 4)])
print("\nArray as DataFrame:")
print(array_df)

# Converting dictionary to DataFrame
dict_df = pd.DataFrame(my_dict, index=[f'Index{i}' for i in range(1, len(my_dict['a']) + 1)])
print("\nDictionary as DataFrame:")
print(dict_df)

# Reversing and displaying each
reversed_list = my_list[::-1]
reversed_dict = {key: value[::-1] for key, value in my_dict.items()}
reversed_array = my_array[::-1, ::-1]
reversed_series = my_series[::-1]

# Reversing list to DataFrame
reversed_list_df = pd.DataFrame([reversed_list], index=['Row1'], columns=[f'Col{i}' for i in range(1, len(reversed_list) + 1)])
print("\nReversed List as DataFrame:")
print(reversed_list_df)

# Reversing array to DataFrame
reversed_array_df = pd.DataFrame(reversed_array, index=[f'Row{i}' for i in range(1, 4)], columns=[f'Column{i}' for i in range(1, 4)])
print("\nReversed Array as DataFrame:")
print(reversed_array_df)

# Reversing dictionary to DataFrame
reversed_dict_df = pd.DataFrame(reversed_dict, index=[f'Index{i}' for i in range(1, len(reversed_dict['a']) + 1)])
print("\nReversed Dictionary as DataFrame:")
print(reversed_dict_df)

# Reversing series to DataFrame
reversed_series_df = reversed_series.to_frame('Values')
print("\nReversed Series as DataFrame:")
print(reversed_series_df)
