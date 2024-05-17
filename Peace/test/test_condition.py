import pandas as pd
import shutil
import os

shutil.rmtree('./Peace/test/combine_result', ignore_errors=True)
os.makedirs('./Peace/test/combine_result')

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('.\Peace\condition.xlsx')

#นำเข้ารหัส Product ยกเลิก
cancel_product = pd.read_excel('.\Peace\condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

#นำเข้ารหัสกิจกรรมยกเลิก
cancel_act = pd.read_excel('.\Peace\condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

#เปลี่ยน X เป็น \d เพื่อใช้ใน regex
all_condition['รหัส'] = all_condition['รหัส'].str.replace('X','\d')

#ต้องเช็ค row ใน condition ว่ามีรหัสอะไร และ มีเงื่อนไขอะไร

#ตัวแปรเพื่อเช็คว่าควรเขียน header หรือไม่สำหรับแต่ละไฟล์
write_header_nobp = True
write_header_notrne = True
write_header_notn = True

#ต้องเช็ค row ใน condition มีเงื่อนไขอะไร
for index, row in all_condition.iterrows():
    filtered = dataframe.loc[dataframe['G/L'].str.contains((row['รหัส']), na=False, regex=True)]
    
    if pd.isna(row['เงื่อนไข 2']):
        match row['เงื่อนไข 1']:
            case 'บันทึกรหัสกระบวนการทางธุรกิจ':
                NoBP = filtered[filtered['Bus. Process'].isna()]
                if not NoBP.empty:
                    NoBP.to_csv('./Peace/test/combine_result/NoBP.csv', mode='a', header=write_header_nobp)
                    write_header_nobp = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม R, N, E)':
                NotRNE = filtered.loc[~filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                if not NotRNE.empty:
                    NotRNE.to_csv('./Peace/test/combine_result/NotRNE.csv', mode='a', header=write_header_notrne)
                    write_header_notrne = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (N)':
                NotN = filtered.loc[~filtered['Bus. Process'].str.contains('[N]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                if not NotN.empty:
                    NotN.to_csv('./Peace/test/combine_result/NotN.csv', mode='a', header=write_header_notn)
                    write_header_notn = False
    else :
        print('false')
