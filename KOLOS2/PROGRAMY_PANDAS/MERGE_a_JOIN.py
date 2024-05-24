import pandas as pd

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

# Creating another DataFrame
data2 = {
    'A': [1, 2, 3, 4],
    'E': ['a', 'b', 'c', 'd']
}
df2 = pd.DataFrame(data2)

# Merging DataFrames
merged_df = pd.merge(df, df2, on='A')
print(merged_df)
#    A  B   C  E
# 0  1  5   9  a
# 1  2  6  10  b
# 2  3  7  11  c
# 3  4  8  12  d
print("\n")

# Joining DataFrames
df3 = df.set_index('A')
df4 = df2.set_index('A')
joined_df = df3.join(df4)
print(joined_df)
#    B   C  E
# A          
# 1  5   9  a
# 2  6  10  b
# 3  7  11  c
# 4  8  12  d


