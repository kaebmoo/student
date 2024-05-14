import pandas as pd

dataframe = pd.read_csv('.\Peace\EXP_DATA_30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')
cancel_number = pd.read_excel('.\Peace\condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_number = cancel_number['Act']

condition_13 = all_condition.iloc[12,0]

filtered = dataframe.loc[(dataframe['Bus. Process'].str.contains(cancel_number[39], na=False)) | (dataframe['Bus. Process'].str.contains(cancel_number[40], na=False))]
filtered.to_csv('./Peace/test/result/Cancel_number.csv')

#filtered = dataframe.loc[dataframe['Bus. Process'].str.contains('|'.join(cancel_number), na=False)]
#filtered.to_csv('./Peace/test/result/test_output.csv')