import numpy as np
import pandas as pd



df1 = pd.DataFrame([[2942,9840,2794,8891,8111,2933,8301,9125], ['Sylwia', 'Katarzyna', 'Teresa', 'Tomasz','Cezary', 'Zenon', 'Filip', 'Adrian'],[13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name','Age']
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312,2336,2942,9840,2794,8891,8111,2933],['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa','Tomasz', 'Cezary', 'Zenon'],weight,height,glasses]).T
df2.columns = ['ID','Name','W', 'H','Gl']
print(df1)
print(df2)
