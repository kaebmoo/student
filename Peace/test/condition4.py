import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#เปลี่ยนตัว X เป็น \d จากเงื่อนไขรหัสที่ 4 เพื่อไปใช้ใน regex
condition4 = all_condition.iloc[3,0].replace('X','\d')

#เลือกรหัส 5X602XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition4), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('NoBP_ค่าสวัสดิการ.csv')