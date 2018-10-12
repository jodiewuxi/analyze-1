import json
import pandas as pd
'''
def execute():
    label_N=[]
    label_V=[]

    tx=open(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\mergeddata.json')
    js=json.load(tx)
    i=1
    record_1=js[i]
    print(record_1)
    record_1_datalist=record_1["dataFields"]
    print(record_1_datalist)
    for lbl_dic in record_1_datalist:
        label_N.append(lbl_dic['name'])
    label_N.sort()
    print(label_N)
    df=pd.DataFrame(label_N)
    df.to_csv(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\labelCsv_JOSN_sort.csv')

def excute1():
    lbl=pd.read_csv(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\labelCsv.txt',names=['lblname'])
    lbl.sort_index(axis=1, ascending=False)
    print(lbl.sort_values(by='lblname'))
    sort_lbl=lbl.sort_values(by='lblname')
    sort_lbl.to_csv(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\labelCsv_sort.csv')

if __name__ == '__main__':
    excute1()
'''


tx=open(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\mergeddata.json')
js=json.load(tx)
i=1
record_1=js[i]
print(record_1)
record_1_datalist=record_1["dataFields"]
writer = pd.ExcelWriter(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\output.xls')
'''
for i in range(12):
    record_1=js[i]
    record_1_datalist=record_1["dataFields"]
'''
label_N=[]
label_V=[]
for lbl_dic in record_1_datalist:
    label_N.append(lbl_dic['name'])
    lbl_series_list=lbl_dic['series']
    lbl_series_value=[]
    for lbl_series in lbl_series_list:
        lbl_series_value.append(lbl_series['value'])
    label_V.append(lbl_series_value)

df=pd.DataFrame(label_V,index=label_N,)
print(df)
df.to_excel(writer,'Sheet'+str(i+1))
writer.save()

