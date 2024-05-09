import pandas as pd

data_name = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge1')
data_nation = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge2')
data_nation2 = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge3')

##เลือกเฉพาะข้อมูลจากด้านซ้าย
#print(data_name.merge(data_nation, how='left', on='Nationality'))

##เลือกเฉพาะข้อมูลจากด้านขวา
print(data_name.merge(data_nation, how='right', on='Nationality')[0:30])

##เลือกเฉพาะข้อมูลที่ตรงกันทั้ง 2 ฝั่ง
#print(data_name.merge(data_nation, how='inner', on='Nationality'))

##เลือกเฉพาะข้อมูลที่ไม่ตรงกับด้านขวา
