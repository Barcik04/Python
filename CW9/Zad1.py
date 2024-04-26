import numpy as np
import pandas as pd

data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
string_data = np.array(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"])
seria = pd.Series(string_data)


my_list = ["red", "blue", "green", "yellow", "black"]
my_series = pd.Series(my_list)

# Converting the Series back to a list
converted_list = my_series.tolist()


numpy_array = np.array([10, 20, 30, 40, 50])
series_from_array = pd.Series(numpy_array)


numpy_array_from_series = my_series.to_numpy()





series1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Perform arithmetic operations
addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2

# Display the results
print("Addition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)



import numpy as np
import pandas as pd

random_numbers = np.random.choice(np.arange(-10, 10.1, 0.1), 10, replace=False)

series = pd.Series(random_numbers)


negative_numbers = series[series < 0]


print("Initial Series of random numbers:")
print(series)
print("\nSeries with negative numbers only:")
print(negative_numbers)



