import pandas as pd
import shutil
import os

def setup_output_directory(directory_path):
    shutil.rmtree(directory_path, ignore_errors=True)
    os.makedirs(directory_path)

def load_data():
    condition_table = pd.read_excel('./Peace/condition.xlsx', dtype=str)
    main_df = pd.read_csv('./Peace/30042024.csv', dtype=str)
    account_name = pd.read_excel('./Peace/รหัสศูนย์ต้นทุน-รหัสบัญชี.xlsx', 'G L', dtype=str)
    cancel_product = pd.read_excel('./Peace/condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)['รหัส']
    cancel_act = pd.read_excel('./Peace/condition.xlsx', 'รหัสกิจกรรมยกเลิก')['Act']
    return condition_table, main_df, account_name, cancel_product, cancel_act

def merge_account_name(main_df, account_name):
    main_df = pd.merge(main_df.drop(columns=['Stat']), account_name, on='G/L', how='left')
    col = main_df.pop('Stat')
    main_df.insert(1, col.name, col)
    return main_df

def preprocess_conditions(condition_table):
    condition_table['รหัส'] = condition_table['รหัส'].str.replace('X', '\\d')
    return condition_table

def apply_conditions(main_df, condition_table, cancel_product, cancel_act, output_directory):
    for index, row in condition_table.iterrows():
        find_pattern = row['find']
        exclude_pattern = row['exclude']
        filtered_df = main_df.loc[main_df['G/L'].str.contains(row['รหัส'], na=False, regex=True)]

        if pd.notna(exclude_pattern):
            filtered_df = filtered_df.loc[~filtered_df['G/L'].str.contains(exclude_pattern, na=False)]

        if pd.notna(find_pattern):
            if 'product ' in find_pattern.lower():
                product_code = ''.join(filter(str.isdigit, find_pattern))
                filtered_df = filtered_df[filtered_df['ผลิตภัณฑ์/'].str.contains(product_code, na=False)]
            elif 'cancel_product' in find_pattern.lower():
                filtered_df = filtered_df.loc[filtered_df['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
            elif 'cancel_act' in find_pattern.lower():
                filtered_df = filtered_df.loc[filtered_df['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]
            else:
                filtered_df = filtered_df.loc[filtered_df['Bus. Process'].str.contains(find_pattern, na=False, regex=True)]

        output_path = os.path.join(output_directory, f'result_{index + 1}.csv')
        filtered_df.to_csv(output_path, index=False)

def main():
    output_directory = './Peace/test/All_condition_result'
    setup_output_directory(output_directory)
    condition_table, main_df, account_name, cancel_product, cancel_act = load_data()
    main_df = merge_account_name(main_df, account_name)
    condition_table = preprocess_conditions(condition_table)
    apply_conditions(main_df, condition_table, cancel_product, cancel_act, output_directory)
    print("Filtering and saving completed.")

if __name__ == "__main__":
    main()