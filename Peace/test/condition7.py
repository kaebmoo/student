import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

filtered_1 = dataframe.loc[~dataframe['G/L'].str.contains('51642196','51642197')]

condition7 = all_condition.iloc[6,0].replace('X','\d')

#เลือกรหัส 5X642XXX
filtered_2 = filtered_1.loc[filtered_1['G/L'].str.contains((condition7), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered_2[filtered_2['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_ซ่อมแซมและบำรุงรักษา.csv')