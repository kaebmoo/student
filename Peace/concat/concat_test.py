import pandas as pd

#ชุดข้อมูล A
data_athlete1 = pd.read_excel('.\Peace\sampledata.xlsx','Athletes_name1')
#ชุดข้อมูล B
data_athlete2 = pd.read_excel('.\Peace\sampledata.xlsx','Athletes_name2')
#ชุดข้อมูล C
data_alphacode = pd.read_excel('.\Peace\sampledata.xlsx','alpha_code')

##concat เรียงต่อกัน
#print(pd.concat([data_athlete1,data_athlete2]))

##เรียง index ใหม่
concat_result = pd.concat([data_athlete1,data_athlete2], ignore_index=True)
#print(concat_result)

##concat ไม่เรียงต่อกัน
#print(pd.concat([concat_result,data_alphacode]))

##concat horizontal
print(pd.concat([concat_result,data_alphacode], axis=1))