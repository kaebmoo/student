import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv', dtype=str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')
cancel_product = pd.read_excel('.\Peace\condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

condition22 = all_condition.iloc[21,0].replace('X','\d')

#กรองเฉพาะ G/L 5XXXXXXX
filtered_1 = dataframe.loc[dataframe['G/L'].str.contains((condition22), regex=True)]

#กรองเฉพาะ record ที่มีรหัสผลิตภัณฑ์ยกเลิก
filtered_2 = filtered_1.loc[filtered_1['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
filtered_2.to_csv('./Peace/test/result/Cancel_product.csv')

#filtered = dataframe.loc[dataframe['Bus. Process'].str.contains('|'.join(cancel_number), na=False)]
#filtered.to_csv('./Peace/test/result/test_output.csv')