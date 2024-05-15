import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#นำเข้ารหัส Product ยกเลิก
cancel_product = pd.read_excel('.\Peace\condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

#นำเข้ารหัสกิจกรรมยกเลิก
cancel_act = pd.read_excel('.\Peace\condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

#เปลี่ยน X เป็น \d เพื่อใช้ใน regex
condition_code = all_condition['รหัส'].str.replace('X','\d')

print(condition_code)

#ต้องเช็ค row ใน condition ว่ามีรหัสอะไร และ มีเงื่อนไขอะไร
#



# def match_exclude(row, all_condition):
#     for pattern in all_condition['รหัส'] :
#         if row['G/L'].match(pattern):
#             return True
#     return False

# df = dataframe[~dataframe.apply(lambda row: match_exclude(row, all_condition), axis=1)].reset_index(drop=True)
# print(df)