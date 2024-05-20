import pandas as pd
import shutil
import os

shutil.rmtree('./Peace/test/combine_result', ignore_errors=True)
os.makedirs('./Peace/test/combine_result')

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('./Peace/condition.xlsx')

#ใส่ชื่อบัญชี
account_name = pd.read_excel('./Peace/รหัสศูนย์ต้นทุน-รหัสบัญชี.xlsx', 'G L', dtype=str)
dataframe = pd.merge(dataframe.drop(columns=['Stat']), account_name, on='G/L', how='left')
col = dataframe.pop('Stat')
dataframe.insert(1, col.name, col)

#นำเข้ารหัส Product ยกเลิก
cancel_product = pd.read_excel('./Peace/condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

#นำเข้ารหัสกิจกรรมยกเลิก
cancel_act = pd.read_excel('./Peace/condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

#เปลี่ยน X เป็น \d เพื่อใช้ใน regex
all_condition['รหัส'] = all_condition['รหัส'].str.replace('X','\d')

#ตัวแปรเพื่อเช็คว่าควรเขียน header หรือไม่สำหรับแต่ละไฟล์
write_header_bp = True
write_header_rne = True
write_header_n = True
write_header_51 = True
write_header_54 = True
write_header_P192 = True
write_header_j = True
write_header_sca = True
write_header_en = True
write_header_ej = True
write_header_scp = True
write_header_cancel_act = True
write_header_bp_ex = True

#ต้องเช็ค row ใน condition มีเงื่อนไขอะไร
for index, row in all_condition.iterrows():
    filtered = dataframe.loc[dataframe['G/L'].str.contains((row['รหัส']), na=False, regex=True)]

    if pd.isna(row['เงื่อนไข 2']):
        match row['เงื่อนไข 1']:
            case 'บันทึกรหัสกระบวนการทางธุรกิจ':
                NoBP = filtered[~filtered['Bus. Process'].isna()]
                NoBP.to_csv('./Peace/test/combine_result/saved_act.csv', mode='a', index = False, header=write_header_bp)
                write_header_bp = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม R, N, E)':
                NotRNE = filtered.loc[filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotRNE.to_csv('./Peace/test/combine_result/act_RNE.csv', mode='a', index = False, header=write_header_rne)
                write_header_rne = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (N)':
                NotN = filtered.loc[filtered['Bus. Process'].str.contains('[N]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotN.to_csv('./Peace/test/combine_result/act_N.csv', mode='a', index = False, header=write_header_n)
                write_header_n = False
            
            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม J)':
                NotJ = filtered.loc[filtered['Bus. Process'].str.contains('[J]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotJ.to_csv('./Peace/test/combine_result/act_J.csv', mode='a', index = False, header=write_header_j)
                write_header_j = False

            case 'รหัสบัญชี 51XXXXXX เท่านั้น':
                filtered = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                Not51 = filtered.loc[filtered['G/L'].str.contains(('^51'), regex=True)]
                Not51.to_csv('./Peace/test/combine_result/GL51.csv', mode='a', index = False, header=write_header_51)
                write_header_51 = False

            case 'รหัสบัญชี 54XXXXXX เท่านั้น':
                filtered = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                Not54 = filtered.loc[filtered['G/L'].str.contains(('^54'), regex=True)]
                Not54.to_csv('./Peace/test/combine_result/GL54.csv', mode='a', index = False, header=write_header_54)
                write_header_54 = False

            case 'บันทึกเข้า Product 192020001':
                NotP = filtered[filtered['ผลิตภัณฑ์/'].str.contains(('192020001'), na=False)]
                NotP.to_csv('./Peace/test/combine_result/Product192020001.csv', index = False, mode='a', header=write_header_P192)
                write_header_P192 = False

            case 'ยกเลิก/ห้ามบันทึก':
                specific_cancel_act = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                specific_cancel_act.to_csv('./Peace/test/combine_result/SCA.csv', index = False, mode='a', header=write_header_sca)
                write_header_sca = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม E, N)':
                NotEN = filtered.loc[filtered['Bus. Process'].str.contains('[EN]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotEN.to_csv('./Peace/test/combine_result/act_EN.csv', mode='a', index = False, header=write_header_en)
                write_header_en = False
                
            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม E, J)':
                NotEJ = filtered.loc[filtered['Bus. Process'].str.contains('[EJ]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotEJ.to_csv('./Peace/test/combine_result/act_EJ.csv', mode='a', index = False, header=write_header_ej)
                write_header_ej = False
            
            case 'ห้ามบันทึกรหัส Product ยกเลิก':
                saved_cancel_product = filtered.loc[~filtered['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
                saved_cancel_product.to_csv('./Peace/test/combine_result/not_cancel_product.csv', mode='a', index = False, header=write_header_scp)
                write_header_scp = False

            case 'ห้ามบันทึกรหัสกิจกรรมที่ยกเลิก':
                saved_cancel_act = filtered.loc[~filtered['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]
                saved_cancel_act.to_csv('./Peace/test/combine_result/not_cancel_act.csv', mode='a', index = False, header=write_header_cancel_act)
                write_header_cancel_act = False

    else :
        excluded = dataframe.loc[~dataframe['G/L'].str.contains('51642196','51642197', na=False)]
        target = excluded.loc[excluded['G/L'].str.contains((row['รหัส']), na=False, regex=True)]
        NoBP_excluded = target[~target['Bus. Process'].isna()]
        NoBP_excluded.to_csv('./Peace/test/combine_result/saved_act_excluded.csv', mode='a', index = False, header=write_header_bp_ex)
        write_header_bp_ex = False