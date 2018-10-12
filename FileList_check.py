import pandas as pd

df = pd.read_excel('D:\LocalData\FJT02454\Documents\mywork\Probe\運用保守\ESBファイル転送履歴_PROBE_BDP_20180629.xlsx')
print(df)

filename=df["FILE_NAME"]
filename_list=filename.tolist()

'''
with open(r'D:\LocalData\FJT02454\Documents\mywork\Probe\運用保守\vNext_filelist.txt', "r") as file:
    data = file.read()
    fileinfo = data.split('\n')

for file_1 in filename_list:
    if file_1 in fileinfo:
        pass
    else:
        print("a file is not inclued")
'''