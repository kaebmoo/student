import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#เลือกรหัส 5X602XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains(('5\d602\d\d\d'), regex=True)]
print(filtered)

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('NoBP_ค่าสวัสดิการ.csv')