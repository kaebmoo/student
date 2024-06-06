import pandas as pd

df = pd.read_csv('./Peace/replace/CONTRACT_PACKAGE_NAME.csv', dtype=str)

print(df)
df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.replace(r'^\s*[A-Z0-9_]+(?:\s+[A-Z0-9_]+)?(?:\s*\([^)]+\))?(\s*:\s*|\s*:)', '', regex=True)
df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.replace(r'ค่าบริการ', '', regex=True)
df['CONTRACRT NAME TH'] = df['CONTRACRT NAME TH'].str.strip()
print(df)

df.to_csv('./Peace/replace/CONTRACT_PACKAGE_NAME_20240605.csv', index=False)