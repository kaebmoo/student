import pandas as pd

df = pd.read_excel('./Peace/test/PACKAGE_CATEGORY.xlsx', dtype=str)

df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.replace(r'^[A-Z0-9]+ : ', '', regex=True)
print(df)

df.to_excel('./Peace/test/result.xlsx', index=False)