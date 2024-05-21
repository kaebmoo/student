import pandas as pd

def regex_filter(df1, df2):
    mask = pd.Series([False] * len(df1))
    for _, regex_row in df2.iterrows():
        gl_mask = df1['G/L'].str.contains(regex_row['G/L (regex)'], regex=True)
        activity_mask = df1['ACTIVITY'].str.contains(regex_row['ACTIVITY (regex)'], regex=True)
        mask = mask | (gl_mask & activity_mask)
    return df1[mask]


df = pd.read_csv(r"Peace/30042024.csv", dtype=str)
df_condition = pd.read_csv(r"Seal/MASTER_CONDITIONS.csv", dtype=str)
df_gl_bp = pd.read_csv(r"Seal/MASTER_GL_BP.csv", dtype=str)

print(df.dtypes)
print(df_condition.dtypes)

df["ACTIVITY"] = df["Bus. Process"].str[-5:].fillna("")

# Ensure all values in the relevant columns are strings
df['G/L'] = df['G/L'].astype(str)
df['ACTIVITY'] = df['ACTIVITY'].astype(str)
filtered_df1 = df[df['ACTIVITY'] != ""]
print(filtered_df1)
# Apply the function to filter filtered_df1
filtered_df1 = regex_filter(filtered_df1, df_condition)

# Print the filtered dataframe
print(filtered_df1)

# Extract regex patterns from df_gl_bp
regex_gl = df_gl_bp['G/L (regex)'].tolist()
# Create a combined regex pattern
combined_regex = "|".join(regex_gl)

# หา gl ที่ match กับ gl 
# Filter the dataframe based on the combined regex pattern
# filtered_df_bp = df[df['G/L'].str.match(combined_regex, na=False)].reset_index(drop=True)
filtered_df_bp = df[df['G/L'].str.match(combined_regex, na=False)]

# GL ที่ต้องบันทึกกระบวนการทางธุรกิจเท่านั้น ถ้าไม่ได้บันทึกเท่ากับผิด
df_filtered_null = filtered_df_bp[filtered_df_bp['ACTIVITY'].isnull()]
print(df_filtered_null)

result = pd.concat([filtered_df1, df_filtered_null])

result.to_excel(r"Seal/result.xlsx")