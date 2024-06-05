import pandas as pd

dataframe = pd.read_csv('./Peace/30042024.csv')
dataframe['G/L'] = dataframe['G/L'].apply(str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#เปลี่ยนตัว X เป็น \d จากเงื่อนไขรหัสที่ 4 เพื่อไปใช้ใน regex
condition4 = all_condition.iloc[3,0].replace('X','\d')

#เลือกรหัส 5X602XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition4), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_ค่าสวัสดิการ.csv')

#-------------------------------------------------------------------------------------------------#

condition5 = all_condition.iloc[4,0].replace('X','\d')

#เลือกรหัส 5X603XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition5), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_ฝึกอบรมบุคลากร.csv')

#-------------------------------------------------------------------------------------------------#

condition6 = all_condition.iloc[5,0].replace('X','\d')

#เลือกรหัส 5X604XXX
filtered = dataframe.loc[dataframe['G/L'].str.contains((condition6), regex=True)]

#นำ record ที่ไม่มีรหัสกระบวนการทางธุรกิจ ออก
NoBP = filtered[filtered['Bus. Process'].isna()]
NoBP.to_csv('./Peace/test/result/NoBP_เดินทางเพื่อปฏิบัติงาน.csv')