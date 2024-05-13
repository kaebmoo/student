import pandas as pd

# Create DataFrames from the lists
df_A = pd.DataFrame({'A': [5, 7, 8, 6, 3, 2]})
df_B = pd.DataFrame({'B': [5, 9, 10, 2, 3]})

# Identify values in A that are not in B
unmatched_values = df_A['A'].loc[~df_A['A'].isin(df_B['B'])]


# Display the unmatched values
print(unmatched_values)

unmatched_values = df_B['B'].loc[~df_B['B'].isin(df_A['A'])]

print(unmatched_values)

print(~df_B['B'].isin(df_A['A']))