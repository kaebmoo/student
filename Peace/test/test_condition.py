import pandas as pd
import shutil
import os

shutil.rmtree('./Peace/test/combine_result', ignore_errors=True)
os.makedirs('./Peace/test/combine_result')

dataframe = pd.read_csv('./Peace/30042024.csv', dtype=str)
all_condition = pd.read_excel('./Peace/condition.xlsx')

#นำเข้ารหัส Product ยกเลิก
cancel_product = pd.read_excel('./Peace/condition.xlsx', 'รหัส Product ยกเลิก', dtype=str)
cancel_product = cancel_product['รหัส']

#นำเข้ารหัสกิจกรรมยกเลิก
cancel_act = pd.read_excel('./Peace/condition.xlsx', 'รหัสกิจกรรมยกเลิก')
cancel_act = cancel_act['Act']

#เปลี่ยน X เป็น \d เพื่อใช้ใน regex
all_condition['รหัส'] = all_condition['รหัส'].str.replace('X','\d')

#ตัวแปรเพื่อเช็คว่าควรเขียน header หรือไม่สำหรับแต่ละไฟล์
write_header_nobp = True
write_header_notrne = True
write_header_notn = True
write_header_not51 = True
write_header_not54 = True
write_header_notP192 = True
write_header_notj = True
write_header_sca = True
write_header_noten = True
write_header_notej = True
write_header_scp = True
write_header_cancel_act = True
write_header_nobp_ex = True

#print(all_condition['เงื่อนไข 1'].str[10:12])

#ต้องเช็ค row ใน condition มีเงื่อนไขอะไร
for index, row in all_condition.iterrows():
    filtered = dataframe.loc[dataframe['G/L'].str.contains((row['รหัส']), na=False, regex=True)]

    if pd.isna(row['เงื่อนไข 2']):
        match row['เงื่อนไข 1']:
            case 'บันทึกรหัสกระบวนการทางธุรกิจ':
                NoBP = filtered[filtered['Bus. Process'].isna()]
                NoBP.to_csv('./Peace/test/combine_result/NoBP.csv', mode='a', index_label='Index', header=write_header_nobp)
                write_header_nobp = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม R, N, E)':
                NotRNE = filtered.loc[~filtered['Bus. Process'].str.contains('[RNE]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotRNE.to_csv('./Peace/test/combine_result/NotRNE.csv', mode='a', index_label='Index', header=write_header_notrne)
                write_header_notrne = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (N)':
                NotN = filtered.loc[~filtered['Bus. Process'].str.contains('[N]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotN.to_csv('./Peace/test/combine_result/NotN.csv', mode='a', index_label='Index', header=write_header_notn)
                write_header_notn = False
            
            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม J)':
                NotJ = filtered.loc[~filtered['Bus. Process'].str.contains('[J]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotJ.to_csv('./Peace/test/combine_result/NotJ.csv', mode='a', index_label='Index', header=write_header_notj)
                write_header_notj = False

            case 'รหัสบัญชี 51XXXXXX เท่านั้น':
                filtered = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                Not51 = filtered.loc[~filtered['G/L'].str.contains(('^51'), regex=True)]
                Not51.to_csv('./Peace/test/combine_result/Not51.csv', mode='a', index_label='Index', header=write_header_not51)
                write_header_not51 = False

            case 'รหัสบัญชี 54XXXXXX เท่านั้น':
                filtered = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                Not54 = filtered.loc[~filtered['G/L'].str.contains(('^54'), regex=True)]
                Not54.to_csv('./Peace/test/combine_result/Not54.csv', mode='a', index_label='Index', header=write_header_not54)
                write_header_not54 = False

            case 'บันทึกเข้า Product 192020001':
                NotP = filtered[~filtered['ผลิตภัณฑ์/'].str.contains(('192020001'), na=False)]
                NotP.to_csv('./Peace/test/combine_result/NotProduct192020001.csv', index_label='Index', mode='a', header=write_header_notP192)
                write_header_notP192 = False

            case 'ยกเลิก/ห้ามบันทึก':
                specific_cancel_act = dataframe.loc[dataframe['Bus. Process'].str.contains((row['รหัส']+'$'), na=False, regex=True)]
                specific_cancel_act.to_csv('./Peace/test/combine_result/SCA.csv', index_label='Index', mode='a', header=write_header_sca)
                write_header_sca = False

            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม E, N)':
                NotEN = filtered.loc[~filtered['Bus. Process'].str.contains('[EN]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotEN.to_csv('./Peace/test/combine_result/NotEN.csv', index_label='Index', mode='a', header=write_header_noten)
                write_header_noten = False
                
            case 'บันทึกรหัสกระบวนการทางธุรกิจ (กิจกรรม E, J)':
                NotEJ = filtered.loc[~filtered['Bus. Process'].str.contains('[EJ]{1}[A-Z0-9]{4}$', na=False, regex=True)]
                NotEJ.to_csv('./Peace/test/combine_result/NotEJ.csv', index_label='Index', mode='a', header=write_header_notej)
                write_header_notej = False
            
            case 'ห้ามบันทึกรหัส Product ยกเลิก':
                saved_cancel_product = filtered.loc[filtered['ผลิตภัณฑ์/'].str.contains('|'.join(cancel_product), na=False)]
                saved_cancel_product.to_csv('./Peace/test/combine_result/Cancel_product.csv', index_label='Index', mode='a', header=write_header_scp)
                write_header_scp = False

            case 'ห้ามบันทึกรหัสกิจกรรมที่ยกเลิก':
                saved_cancel_act = filtered.loc[filtered['Bus. Process'].str.contains('|'.join(cancel_act), na=False)]
                saved_cancel_act.to_csv('./Peace/test/combine_result/Cancel_act.csv', index_label='Index', mode='a', header=write_header_cancel_act)
                write_header_cancel_act = False

    else :
        excluded = dataframe.loc[~dataframe['G/L'].str.contains('51642196','51642197', na=False)]
        target = excluded.loc[excluded['G/L'].str.contains((row['รหัส']), na=False, regex=True)]
        NoBP_excluded = target[target['Bus. Process'].isna()]
        NoBP_excluded.to_csv('./Peace/test/combine_result/NoBP_excluded.csv', index_label='Index', mode='a', header=write_header_nobp_ex)
        write_header_nobp_ex = False