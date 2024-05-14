import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#เปลี่ยนตัว X เป็น \d จากเงื่อนไขรหัสที่ 1 เพื่อไปใช้ใน regex
condition1 = all_condition.iloc[0,0].replace('X','\d')

#เลือกรหัส 516017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition1), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม R, N, E ออกมา
NotRNE = filtered.loc[~filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotRNE.to_csv('NotRNE_result.csv')