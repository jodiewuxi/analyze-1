import pandas as pd

df=pd.read_csv('D:\LocalData\FJT02454\Documents\mywork\Probe\GEN2_ProbeData_20180711015056_PMA-PAAA-01G-001.tsv',sep='\t',header=None,dtype=str)

df_tr=df.iloc[0:,2:3]
print(dir(pd.DataFrame))
help(pd.DataFrame.mean)