import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
condition1 = pd.read_excel('.\Peace\condition.xlsx')

#เลือกรหัส 516017XX
filtered = dataframe.loc[dataframe['G/L'].str.contains('^516017\d{2}$', regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม R, N, E ออกมา
NotRNE = filtered.loc[~filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotRNE.to_csv('NotRNE_result.csv')