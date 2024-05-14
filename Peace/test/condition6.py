import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition6 = all_condition.iloc[5,0].replace('X','\d')

#เลือกรหัส 5X604XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition6), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_เดินทางเพื่อปฏิบัติงาน.csv')