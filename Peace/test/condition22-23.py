import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')
cancel_product = pd.read_excel('.\Peace\condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

condition22 = all_condition.iloc[21,0].replace('X','\d')

#กรองเฉพาะ G/L 5XXXXXXX
filtered22_1 = dataframe.loc[dataframe['G/L'].str.contains((condition22), na=False, regex=True)]

#กรองเฉพาะ record ที่มีรหัสผลิตภัณฑ์ยกเลิก
filtered22_2 = filtered22_1.loc[filtered22_1['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
filtered22_2.to_csv('./Peace/test/result/Cancel_product.csv')

#-------------------------------------------------------------------------------------------------#

cancel_act = pd.read_excel('.\Peace\condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

condition23 = all_condition.iloc[22,0].replace('X','\d')

filtered23_1 = dataframe.loc[dataframe['G/L'].str.contains((condition22), na=False, regex=True)]

filtered23_2 = filtered23_1.loc[filtered23_1['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]
filtered23_2.to_csv('./Peace/test/result/Cancel_act.csv')