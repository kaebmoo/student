import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition20 = all_condition.iloc[19,0].replace('X','\d')

#เลือกรหัส 5X642108
filtered20 = dataframe.loc[dataframe['G/L'].str.contains((condition20), regex=True)]

#นำ record ที่ไม่มีรหัสกิจกรรม E, N ออกมา
NotEN = filtered20.loc[~filtered20['Bus. Process'].str.contains('[EN]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotEN.to_csv('./Peace/test/result/NotEN_result.csv')

#-------------------------------------------------------------------------------------------------#

condition21 = all_condition.iloc[20,0].replace('X','\d')

filtered21 = dataframe.loc[dataframe['G/L'].str.contains((condition21), regex=True)]

NotEJ = filtered21.loc[~filtered21['Bus. Process'].str.contains('[EJ]{1}[A-Z0-9]{4}$', na=False, regex=True)]
NotEJ.to_csv('./Peace/test/result/NotEJ_result.csv')