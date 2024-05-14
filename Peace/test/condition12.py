import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition12 = all_condition.iloc[11,0].replace('X','\d')

#เลือกรหัส 546017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition12), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม J ออกมา
NotN = filtered.loc[~filtered['Bus. Process'].str.contains('[J]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotN.to_csv('./Peace/test/result/NotJ_result.csv')