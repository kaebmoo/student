import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition10 = all_condition.iloc[9,0]

#เลือก record ที่มีรหัสกิจกรรม N0105
filtered_1 = dataframe.loc[dataframe['Bus. Process'].str.contains((condition10+'$'), na=False, regex=True)]

#นำ record ที่รหัสบัญชี != 54XXXXXX
filtered_2 = filtered_1.loc[~filtered_1['G/L'].str.contains(('^54'), regex=True)]
filtered_2.to_csv('./Peace/test/result/N0105_Not54.csv')