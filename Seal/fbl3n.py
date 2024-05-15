# fbl3n
# การแสดงรายการบรรทัดบัญชีแยกประเภททั่วไป
import os
from pathlib import Path
import pandas as pd

def convert_fbl3n(input_path, input_file, ouput_path, output_file):

    df1 = pd.read_csv(Path(os.path.join(input_path, input_file)), skiprows=4, dtype=str, delimiter="\t", encoding="UTF-16")
    print(df1.info())

    condition = df1["บันทึกแล้ว"].isnull()
    df1 = df1.drop(df1[condition].index)
    # Drop columns with null values in place
    df1.dropna(axis=1, inplace=True, how="all")

    df1.to_csv(Path(os.path.join(ouput_path, output_file)), index=False)

    return df1

# "/Users/seal/OneDrive/share/Datasource/2023/expense/EXP._07-12.2023.csv"
# "/Users/seal/OneDrive/share/Datasource/2023/expense/EXP._01-12.2023.csv"

path = "/Users/seal/OneDrive/share/Datasource/adhoc/expense/"
input_file = "30042024.xls"
output_file = "EXP_DATA_30042024.csv"
df = convert_fbl3n(path, input_file, path, output_file)
print(df.info())