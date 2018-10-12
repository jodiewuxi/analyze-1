import pandas as pd
from openpyxl.workbook import Workbook

df=pd.read_csv(r'D:\LocalData\FJT02454\Desktop\logAnalyze\CW_ProbeData_20180709224509_PASDASI3.tsv',sep='\t',encoding='utf-8')
writer = pd.ExcelWriter('D:\LocalData\FJT02454\Desktop\logAnalyze\output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()