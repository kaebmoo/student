import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')
cancel_number = pd.read_excel('.\Peace\condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_number = cancel_number['Act']

filtered = dataframe.loc[(dataframe['Bus. Process'].str.contains(cancel_number[39], na=False)) | (dataframe['Bus. Process'].str.contains(cancel_number[40], na=False))]
filtered.to_csv('./Peace/test/result/Cancel_number.csv')

#filtered = dataframe.loc[dataframe['Bus. Process'].str.contains('|'.join(cancel_number), na=False)]
#filtered.to_csv('./Peace/test/result/test_output.csv')