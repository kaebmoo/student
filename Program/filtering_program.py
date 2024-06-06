import pandas as pd
import shutil
import os
import re
from pathlib import Path

# ตารางเงื่อนไข
condition_table = pd.read_excel('./Program/condition.xlsx', dtype=str)

# ข้อมูลที่ต้องการนำมากรอง
main_df = pd.read_csv('./Program/data.csv', dtype=str)

# ตารางรหัสศูนย์ต้นทุน-รหัสบัญชี
account_name = pd.read_excel('./Program/รหัสศูนย์ต้นทุน-รหัสบัญชี.xlsx', 'G L', dtype=str)

# ตารางรวมรหัส กิจกรรม, Product ยกเลิก
cancel_product = pd.read_excel('./Program/condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)['รหัส']
cancel_act = pd.read_excel('./Program/condition.xlsx', 'รหัสกิจกรรมยกเลิก')['Act']

# ---------------------------------------------------------------------------------------------------#

# สำหรับใส่ชื่อ G/L ในคอลัมน์ stat
main_df = pd.merge(main_df.drop(columns=['Stat']), account_name, on='G/L', how='left')
col = main_df.pop('Stat')
main_df.insert(1, col.name, col)

def setup_output_directory(directory_path):
    shutil.rmtree(directory_path, ignore_errors=True)
    Path(directory_path).mkdir(parents=True, exist_ok=True)

# เปลี่ยน X,x ในตารางเงื่อนไขเป็น \d เพื่อใช้ใน regex
condition_table['รหัส'] = condition_table['รหัส'].apply(lambda x: re.sub(r'[Xx]', r'\\d', x))

def apply_conditions(main_df, condition_table, cancel_product, cancel_act, output_directory):
    write_header = True
    for index, row in condition_table.iterrows():
        find_pattern = row['find']
        exclude_pattern = row['exclude G/L']
        filtered_df = main_df.loc[main_df['G/L'].str.contains(row['รหัส'], na=False, regex=True)]

        if pd.notna(exclude_pattern):
            filtered_df = filtered_df.loc[~filtered_df['G/L'].str.contains(exclude_pattern, na=False)]

        if pd.notna(find_pattern):
            if 'segment ' in find_pattern.lower():
                segment_code = ''.join(filter(str.isdigit, find_pattern))
                filtered_segment = main_df.loc[main_df['เซกเมนต์'].str.contains(segment_code, na=False)]
                filtered_segment = filtered_segment.loc[~filtered_segment['G/L'].str.contains(row['รหัส'], na=False, regex=True)]
                filtered_df = filtered_df.loc[~filtered_df['เซกเมนต์'].str.contains(segment_code, na=False)]
                filtered_df = pd.concat([filtered_segment, filtered_df])

            elif 'act ' in find_pattern.lower():
                act_code = find_pattern.split()[1]
                filtered_act = main_df.loc[main_df['Bus. Process'].str.contains(act_code, na=False)]
                filtered_df = filtered_act.loc[~filtered_act['G/L'].str.contains(row['รหัส'], na=False, regex=True)]

            elif 'cancel_product' in find_pattern.lower():
                filtered_df = filtered_df.loc[filtered_df['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
            elif 'cancel_act' in find_pattern.lower():
                filtered_df = filtered_df.loc[filtered_df['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]
            else:
                filtered_df = filtered_df.loc[filtered_df['Bus. Process'].str.contains(find_pattern, na=False, regex=True)]
        else:
            filtered_df = filtered_df.loc[filtered_df['Bus. Process'].isna()]

        #เพิ่มคอลัมน์ 'เงื่อนไข' ลงใน DataFrame ที่กรองแล้ว
        filtered_df = filtered_df.assign(เงื่อนไข1 = row['เงื่อนไข 1'])
        filtered_df = filtered_df.assign(เงื่อนไข2 = row['เงื่อนไข 2'])

        output_path = os.path.join(output_directory, f'result_{index + 1}.csv')
        output_path_combine = os.path.join(output_directory, f'combine_result.csv')
        filtered_df.to_csv(output_path, index=False)
        filtered_df.to_csv(output_path_combine, mode='a', index = False, header=write_header)
        write_header = False

def main():
    #ตั้งค่าโฟลเดอร์ผลลัพธ์
    output_directory = './Program/Filter_result'
    setup_output_directory(output_directory)
    apply_conditions(main_df, condition_table, cancel_product, cancel_act, output_directory)
    print("Filtering and saving completed.")

if __name__ == "__main__":
    main()