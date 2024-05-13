import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
condition1 = pd.read_excel('.\Peace\condition.xlsx')

#ลบตัว X ออกจากเงื่อนไขรหัสที่ 1
condition1 = condition1.iloc[0,0].replace('X','')

#เลือกรหัส 516017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains(('^'+condition1+'\d{2}$'), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม R, N, E ออกมา
NotRNE = filtered.loc[~filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotRNE.to_csv('NotRNE_result.csv')