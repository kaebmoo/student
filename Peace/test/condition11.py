import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

condition11 = all_condition.iloc[10,0].replace('X','\d')

#เลือกรหัส 59XXXXXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition11), na=False, regex=True)]

#นำ record ที่ไม่บันทึกเข้า Product 192020001 ออก
NotP = filtered[~filtered['ผลิตภัณฑ์/'].str.contains(('192020001'), na=False)]
NotP.to_csv('./Peace/test/result/NotProduct192020001.csv')