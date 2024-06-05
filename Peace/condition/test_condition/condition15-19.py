import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition15 = all_condition.iloc[14,0].replace('X','\d')

filtered15 = dataframe.loc[dataframe['G/L'].str.contains((condition15), regex=True)]

NoBP = filtered15[filtered15['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_อุปกรณ์และสายเคเบิล.csv')

#-------------------------------------------------------------------------------------------------#

condition16 = all_condition.iloc[15,0].replace('X','\d')

filtered16 = dataframe.loc[dataframe['G/L'].str.contains((condition16), regex=True)]

NoBP = filtered16[filtered16['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_วัสดุทั่วไป.csv')

#-------------------------------------------------------------------------------------------------#

condition17 = all_condition.iloc[16,0].replace('X','\d')

filtered17 = dataframe.loc[dataframe['G/L'].str.contains((condition17), regex=True)]

NoBP = filtered17[filtered17['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_วัสดุแบบพิมพ์ใช้ไป.csv')

#-------------------------------------------------------------------------------------------------#

condition18 = all_condition.iloc[17,0].replace('X','\d')

filtered18 = dataframe.loc[dataframe['G/L'].str.contains((condition18), regex=True)]

NoBP = filtered18[filtered18['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_วัสดุแบบพิมพ์-จัดหาเอง.csv')

#-------------------------------------------------------------------------------------------------#

condition19 = all_condition.iloc[18,0].replace('X','\d')

filtered19 = dataframe.loc[dataframe['G/L'].str.contains((condition19), regex=True)]

NoBP = filtered19[filtered19['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_สาธารณูปโภค.csv')