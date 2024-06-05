import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition8 = all_condition.iloc[7,0]

#เลือก record ที่มีรหัสกิจกรรม N0301
filtered_1 = dataframe.loc[dataframe['Bus. Process'].str.contains((condition8+'$'), na=False, regex=True)]

#นำ record ที่รหัสบัญชี != 51XXXXXX
filtered_2 = filtered_1.loc[~filtered_1['G/L'].str.contains(('^51'), regex=True)]
filtered_2.to_csv('./Peace/test/result/N0301_Not51.csv')