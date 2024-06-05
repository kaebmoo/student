import pandas as pd

df = pd.read_excel('./Peace/replace/PACKAGE_CATEGORY.xlsx', dtype=str)

df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.replace(r'^[A-Z0-9]+ :', '', regex=True)
df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.replace(r'ค่าบริการ', '', regex=True)
df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.strip()
print(df)

df.to_excel('./Peace/replace/result.xlsx', index=False)