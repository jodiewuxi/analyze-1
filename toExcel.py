import pandas as pd


df=pd.read_csv(r'D:\LocalData\FJT02454\Desktop\20180712\CW_ProbeData_20180711055504_PASDASI3.tsv',sep='\t',dtype=str,header=None,low_memory=False)

writer = pd.ExcelWriter(r'D:\LocalData\FJT02454\Desktop\20180712\output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

#df=pd.read_csv(r'D:\LocalData\FJT02454\Desktop\logAnalyze\GEN1_ProbeData_20180709134504_PMA-PAAA-02G-001.tsv',sep='\t',low_memory=False,header=None)

#df.to_excel('D:\LocalData\FJT02454\Desktop\logAnalyze\output.xlsx',sheet_name='GEN1')