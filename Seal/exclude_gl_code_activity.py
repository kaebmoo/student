import pandas as pd
from pathlib import Path

# ตำแหน่ง และชื่อไฟล์
input_file = r"/Users/seal/Library/CloudStorage/OneDrive-Personal/share/Datasource/2024/co/joint/j0000_202402.csv"
exclude_gl_file = r"/Users/seal/Documents/GitHub/bot_nt/co/joint/exclude_gl_code_joint.csv"

# อ่านข้อมูล ข้าม 3 บรรทัดแรก
df = pd.read_csv(Path(input_file), skiprows=3, converters={"สปก.ต้นทุน": str, "รหัสกิจกรรม": str}, sep="\t") # joint file from SAP
df_ex_gl = pd.read_csv(Path(exclude_gl_file), converters={"รหัสบัญชี": str, "รหัสกิจกรรม": str}) # gl ที่จะตัดออก

# สร้าง list regex จากตารางรหัสบัญชี x หมายถึงเลขอะไรก็ได้ 0-9 แทนด้วย \d ของ regex
regex_ex_gl = list(df_ex_gl["รหัสบัญชี"].str.replace("x", "\d"))

# ฟังก์ชันเพื่อเช็คว่าแถวใดตรงกับรายการที่จะตัดออกหรือไม่
def match_exclude(row, regex_ex_gl, df_ex_gl):
    for pattern in regex_ex_gl:
        if row["สปก.ต้นทุน"].match(pattern):
            if row["รหัสกิจกรรม"] in df_ex_gl[df_ex_gl["รหัสบัญชี"].str.match(pattern)]["รหัสกิจกรรม"].values:
                return True
    return False

# หา gl ที่ match กับ exclude gl และรหัสกิจกรรมเพื่อตัดออก
df = df[~df.apply(lambda row: match_exclude(row, regex_ex_gl, df_ex_gl), axis=1)].reset_index(drop=True)

# แสดงผลลัพธ์
print(df)
