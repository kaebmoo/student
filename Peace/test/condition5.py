import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition5 = all_condition.iloc[4,0].replace('X','\d')

#เลือกรหัส 5X603XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition5), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('NoBP_ฝึกอบรมบุคลากร.csv')