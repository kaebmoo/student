import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

# URL ของหน้า Wikipedia ที่ต้องการดึงข้อมูล
url = "https://th.wikipedia.org/wiki/รายการรหัสไปรษณีย์ไทย"

# ดึงข้อมูลจากหน้าเว็บ
response = requests.get(url)
response.encoding = 'utf-8'  # ตั้งค่า encoding ให้เป็น utf-8
html_content = response.text

# ใช้ BeautifulSoup เพื่ออ่าน HTML
soup = BeautifulSoup(html_content, 'html.parser')

# ใช้ StringIO เพื่อจัดการกับ HTML สตริง
html_string = str(soup)
html_buffer = StringIO(html_string)

# ใช้ pandas เพื่อดึงตารางจากข้อมูล HTML ที่ดึงมา
tables = pd.read_html(html_buffer)

# ตรวจสอบว่ามีตารางจำนวนเท่าใดในหน้า
num_tables = len(tables)

# ดูตัวอย่างของตารางแรก
sample_table = tables[0]

num_tables, sample_table.head()
# print(tables)
# นำทุก tables มาต่อกันเป็น DataFrame
combined_df = pd.concat(tables, ignore_index=True)

# ดูตัวอย่างของตารางที่รวมกัน
print(combined_df.head())

print(combined_df)
combined_df.to_excel("./Peace/test/zipcode/zipcode_wikipedia_.xlsx", index=False)