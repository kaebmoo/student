import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#ลบตัว X ออกจากเงื่อนไขรหัสที่ 3
condition3 = all_condition.iloc[2,0].replace('X','')

#เลือกรหัส 546017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains(('^'+condition3+'\d{2}$'), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม N ออกมา
NotN = filtered.loc[~filtered['Bus. Process'].str.contains('[N]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotN.to_csv('NotN_result546017XX.csv')