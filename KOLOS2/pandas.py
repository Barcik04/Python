CREATING A DATAFRAME
        import pandas as pd

        # Creating a DataFrame from a dictionary
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        }
        
        df = pd.DataFrame(data)
        print(df)
        #   A  B   C
        #0  1  5   9
        #1  2  6  10
        #2  3  7  11
        #3  4  8  12

SELECTING DATA
        # Selecting a single column
        print(df['A'])
        
        # Selecting multiple columns
        print(df[['A', 'B']])
        
        # Selecting rows by index
        print(df.iloc[0:2])  # First two rows
        
        # Selecting rows by label
        print(df.loc[0:2])  # Rows with index 0 to 2 (inclusive)


        data = {
            'A': [1, 2, 2, 4],
            'B': [5, 6, 7, 8],
            'C': [9, 10, 11, 12]
        }
        
        df = pd.DataFrame(data)
        
        # Grouping data by a column and calculating aggregate statistics
        grouped = df.groupby('A').sum()
        print(grouped)
        #     B   C
        # A        
        # 1   5   9
        # 2  13  21
        # 4   8  12
        
        # Aggregating with multiple functions
        grouped = df.groupby('A').agg({'B': 'sum', 'C': 'mean'})
        print(grouped)
        
        #     B     C
        # A          
        # 1   5   9.0
        # 2  13  10.5
        # 4   8  12.0


  FILTERING DATA
        # Filtering rows based on a condition
        filtered_df = df[df['A'] > 2]
        print(filtered_df)
        #   A  B   C
        #2  3  7  11
        #3  4  8  12

        # Filtering with multiple conditions
        filtered_df = df[(df['A'] > 2) & (df['B'] < 8)]
        print(filtered_df)
        #   A  B   C
        #2  3  7  11

  MODIFYING A DATAFRAME
        # Adding a new column
        df['D'] = df['A'] + df['B']
        print(df)
        
        # Modifying an existing column
        df['A'] = df['A'] * 2
        print(df)

        # Dropping a column
        df = df.drop('C', axis=1)
        print(df)

        # Dropping a row by index
        df = df.drop(0, axis=0)
        print(df)


        # Creating a DataFrame with missing values
        data_with_na = {
            'A': [1, 2, None, 4],
            'B': [5, None, 7, 8],
            'C': [9, 10, 11, None]
        }
        df_na = pd.DataFrame(data_with_na)
        print(df_na)
        
        # Dropping rows with missing values
        df_na_dropped = df_na.dropna()
        print(df_na_dropped)
        
        # Filling missing values
        df_na_filled = df_na.fillna(100)
        print(df_na_filled)


READING A FILE
        # Reading from a CSV file
        df = pd.read_csv('data.csv')
        
        # Writing to a CSV file
        df.to_csv('output.csv', index=False)
