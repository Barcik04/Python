import pandas as pd

# DataFrame 1
data1 = {
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['John', 'Jane', 'Jake', 'Jill'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
}
df1 = pd.DataFrame(data1).set_index('EmployeeID')

# DataFrame 2
data2 = {
    'EmployeeID': [101, 102, 105, 104],
    'Age': [28, 34, 40, 30],
    'City': ['New York', 'Los Angeles', 'San Francisco', 'Chicago']
}
df2 = pd.DataFrame(data2).set_index('EmployeeID')

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Łączenie DataFrame'ów
joined_df = df1.join(df2, how='inner')
print("\nPołączony DataFrame:\n", joined_df)
