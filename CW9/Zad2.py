import pandas as pd
import numpy as np

# DataFrames definition
df1 = pd.DataFrame({
    'ID': [2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
    'Name': ['Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon', 'Filip', 'Adrian'],
    'Age': [13, 31, 34, 14, 13, 28, 20, 15]
})
df2 = pd.DataFrame({
    'ID': [2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933],
    'Name': ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon'],
    'W': [65, 80, 64, 69, 74, 61, 66, 61],
    'H': [179, 179, 151, 177, 170, 157, 151, 153],
    'Gl': [False, True, False, True, False, True, False, True]
})

# Perform an inner join
df_inner = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join Table:")
print(df_inner)

# Perform an outer join
df_outer = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join Table:")
print(df_outer)

# Sorting names in df_inner for demonstration (you can choose either df)
df_sorted = df_inner.sort_values(by='Name_x')
print("\nSorted by Name:")
print(df_sorted)

# Names of people who wear glasses
names_with_glasses = df2[df2['Gl']]['Name'].values
print("\nNames of people who wear glasses:")
print(names_with_glasses)

# Names of people aged 20 to 30
names_aged_20_30 = df1[(df1['Age'] >= 20) & (df1['Age'] <= 30)]['Name'].values
print("\nNames of people aged 20 to 30:")
print(names_aged_20_30)


# Merge operations
df_inner = pd.merge(df1, df2, on='ID', how='inner')
df_outer = pd.merge(df1, df2, on='ID', how='outer')

# Choose one to continue your operations; let's use df_inner here
df_merged = df_inner  # You could use df_outer if that fits your case better

# Calculate BMI for each individual in df2
df2['BMI'] = df2['W'] / (df2['H'] / 100) ** 2

# Display BMI for each individual who does not wear glasses
bmi_no_glasses = df2[df2['Gl'] == False][['Name', 'BMI']]
print("BMI of Individuals Not Wearing Glasses:")
print(bmi_no_glasses)

# Display BMI for each individual who wears glasses
bmi_with_glasses = df2[df2['Gl'] == True][['Name', 'BMI']]
print("\nBMI of Individuals Wearing Glasses:")
print(bmi_with_glasses)

# Sorting names in df2
df_sorted = df2.sort_values(by='Name')
print("\nSorted by Name:")
print(df_sorted)

# Names of people who wear glasses
names_with_glasses = df2[df2['Gl']]['Name'].values
print("\nNames of people who wear glasses:")
print(names_with_glasses)

# Names of people aged 20 to 30
names_aged_20_30 = df1[(df1['Age'] >= 20) & (df1['Age'] <= 30)]['Name'].values
print("\nNames of people aged 20 to 30:")
print(names_aged_20_30)
print("\n")

# Ensure 'Age' is in the correct format
df_merged['Age'] = pd.to_numeric(df_merged['Age'], errors='coerce')

# Calculate the average age
average_age = df_merged['Age'].mean()
print(f"Average age from merged data: {average_age:.2f}")

# Add BMI column
df_merged['BMI'] = df_merged['W'] / (df_merged['H'] / 100) ** 2

# Calculate the average age and BMI for those wearing and not wearing glasses
average_age_with_glasses = df_merged[df_merged['Gl']]['Age'].mean()
average_age_without_glasses = df_merged[~df_merged['Gl']]['Age'].mean()
average_bmi_with_glasses = df_merged[df_merged['Gl']]['BMI'].mean()
average_bmi_without_glasses = df_merged[~df_merged['Gl']]['BMI'].mean()

# Print results
print(f"\nAverage age for those wearing glasses: {average_age_with_glasses:.2f}")
print(f"Average age for those not wearing glasses: {average_age_without_glasses:.2f}")
print(f"Average BMI for those wearing glasses: {average_bmi_with_glasses:.2f}")
print(f"Average BMI for those not wearing glasses: {average_bmi_without_glasses:.2f}")
