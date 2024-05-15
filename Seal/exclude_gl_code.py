import pandas as pd
from pathlib import Path

# ตำแหน่ง และชื่อไฟล์
input_file = r"/Users/seal/Library/CloudStorage/OneDrive-Personal/share/Datasource/2024/co/joint/j0000_202402.csv"
exclude_gl_file = r"/Users/seal/Documents/GitHub/bot_nt/co/joint/exclude_gl_code_joint.csv"

# อ่านข้อมูล ข้าม 3 บรรทัดแรก
df = pd.read_csv(Path(input_file), skiprows=3, converters={"สปก.ต้นทุน":str}, sep="\t") # joint file from SAP
df_ex_gl = pd.read_csv(Path(exclude_gl_file), converters={"รหัสบัญชี":str}) # gl ที่จะตัดออก

# สร้าง list regex จากตารางรหัสบัญชี x หมายถึงเลขอะไรก็ได้ 0-9 แทนด้วย \d ของ regex
regex_ex_gl = list(df_ex_gl["รหัสบัญชี"].str.replace("x", "\d"))

# หา gl ที่ match กับ exclude gl เพื่อตัดออก
# https://stackoverflow.com/questions/47011170/multiple-pattern-using-regex-in-pandas
# https://toltman.medium.com/matching-multiple-regex-patterns-in-pandas-121d6127dd47
# print(df[df["สปก.ต้นทุน"].str.match("|".join(regex_ex_gl)) == True])
df = df[df["สปก.ต้นทุน"].str.match("|".join(regex_ex_gl)) == False].reset_index()

