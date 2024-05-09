import pandas as pd

data_name = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge1')
data_nation = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge2')
data_selected_nation = pd.read_excel('./Peace/sampledata.xlsx','sample_for_merge3')

##เลือกเฉพาะข้อมูลจากด้านซ้าย
left_result = data_name.merge(data_selected_nation, how='left', on='Nationality')
#print(left_result)

##เลือกเฉพาะข้อมูลจากด้านขวา
right_result = data_name.merge(data_nation, how='right', on='Nationality')
#print(right_result)

##เลือกเฉพาะข้อมูลที่ตรงกันทั้ง 2 ฝั่ง
both_result = data_name.merge(data_nation, how='inner', on='Nationality')
#print(both_result)

##เลือกเฉพาะข้อมูลที่ไม่ตรงกับด้านขวา
excludeB = left_result[left_result['Alpha code'].isna()]
#print(excludeB)

##เลือกเฉพาะข้อมูลที่ไม่ตรงกับด้านซ้าย
excludeA = right_result[right_result['Name'].isna()]
print(excludeA)