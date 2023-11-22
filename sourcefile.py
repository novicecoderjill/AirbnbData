import pandas as pd
df = pd.read_csv('https://query.data.world/s/5vtbexliqou5ms7t2qnuxn2flnb272?dws=00000')
print(df.head())
# print((type(df)))
# print((df.info()))
# print(len(df)) #7833
# header = df.columns
# print(header)
df2 = df.iloc[0:]

#print(df2.head())

df2 =df2.dropna()
print(df2.head())
# print(len(df2))

# Find rows with empty values (empty strings)
rows_with_empty_values = df2[df2.isnull().any(axis=1) | (df2 == '').any(axis=1)]

# Display or further process the rows with empty values
#print(rows_with_empty_values)
# print(df2[])

# specific_rows = df[df['host_name'] == 'Daniel']
# print(specific_rows)

df2.to_csv('airbnbdatacleaned.txt', index=False)