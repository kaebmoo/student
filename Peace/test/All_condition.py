import pandas as pd
import shutil
import os

shutil.rmtree('./Peace/test/All_condition_result', ignore_errors=True)
os.makedirs('./Peace/test/All_condition_result')

condition_table = pd.read_excel('./Peace/condition.xlsx')
main_df = pd.read_csv('./Peace/30042024.csv', dtype=str)

#ใส่ชื่อบัญชี
account_name = pd.read_excel('./Peace/รหัสศูนย์ต้นทุน-รหัสบัญชี.xlsx', 'G L', dtype=str)
main_df = pd.merge(main_df.drop(columns=['Stat']), account_name, on='G/L', how='left')
col = main_df.pop('Stat')
main_df.insert(1, col.name, col)

#นำเข้ารหัส Product ยกเลิก
cancel_product = pd.read_excel('./Peace/condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

#นำเข้ารหัสกิจกรรมยกเลิก
cancel_act = pd.read_excel('./Peace/condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

#เปลี่ยน X เป็น \d เพื่อใช้ใน regex
condition_table['รหัส'] = condition_table['รหัส'].str.replace('X','\d')

# Iterate over each row in the condition table
for index, row in condition_table.iterrows():
    find_pattern = row['find']
    exclude_pattern = row['exclude']
    filtered_df = main_df.loc[main_df['G/L'].str.contains((row['รหัส']), na=False, regex=True)]

    if pd.notna(exclude_pattern):
        filtered_df = filtered_df.loc[~filtered_df['G/L'].str.contains(exclude_pattern, na=False)]

    if pd.notna(find_pattern):
        if 'product ' in find_pattern.lower():
            find_pattern = str(''.join(filter(str.isdigit, find_pattern)))
            filtered_df = filtered_df[filtered_df['ผลิตภัณฑ์/'].str.contains(find_pattern, na=False)]

        elif 'cancel_product' in find_pattern.lower():
            filtered_df = filtered_df.loc[~filtered_df['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]

        elif 'cancel_act' in find_pattern.lower():
            filtered_df = filtered_df.loc[~filtered_df['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]

        else:
            filtered_df = filtered_df.loc[filtered_df['Bus. Process'].str.contains(find_pattern, na=False, regex=True)]

    output_path = f'./Peace/test/All_condition_result/result_{index+1}.csv'
    filtered_df.to_csv(output_path, index=False)

print("Filtering and saving completed.")