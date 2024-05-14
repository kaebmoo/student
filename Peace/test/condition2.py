import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#เปลี่ยนตัว X เป็น \d จากเงื่อนไขรหัสที่ 2 เพื่อไปใช้ใน regex
condition2 = all_condition.iloc[1,0].replace('X','\d')

#เลือกรหัส 536017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition2), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม N ออกมา
NotN = filtered.loc[~filtered['Bus. Process'].str.contains('[N]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotN.to_csv('NotN_result536017XX.csv')