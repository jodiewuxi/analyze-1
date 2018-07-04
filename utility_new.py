import os
from matplotlib import pyplot
import pandas as pd
from functools import reduce
'''
out_path = r'D:\LocalData\FJT02454\Desktop\logAnalyze\\'
pic_path=r'D:\LocalData\FJT02454\Desktop\logAnalyze\\'
newLineCode = '\n'
'''

out_path = '/export/measure/maintenance/'
newLineCode = '\r\n'
pic_path='/export/measure/pic/'


def logAnalyze(fileType,line ,analyze_datetime):
    OutputList=[]
###TLDP001I001  ZIP 取り込み
    list_TLDP001I001= list(filter(lambda x: x[0]=='TLDP001I001', line))
    if len(list_TLDP001I001) >0:
        tLDP001_FirstAppearIndex = line.index(list_TLDP001I001[0])
        # TLDP001I001がはじめ出た行の以後から、TLDP001I002を収集
        list_TLDP001I002 = list(filter(lambda x: x[0]=='TLDP001I002', line[tLDP001_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP001I001, list_TLDP001I002):
            t_time = timeCaculation(tLDP001,tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('ZIP取り込み       ',str(tLDP001[1]),str(tLDP002[1]),str(t_time)))
###TLDP001I001  ZIP 取り込み

###TLDP002I001  ZIP展開
    list_TLDP002I001= list(filter(lambda x: x[0]=='TLDP002I001', line))
    if len(list_TLDP002I001) > 0:
        tLDP002_FirstAppearIndex = line.index(list_TLDP002I001[0])
        # TLDP002I001がはじめ出た行の以後から、TLDP002I002を収集
        list_TLDP002I002 = list(filter(lambda x: x[0]=='TLDP002I002', line[tLDP002_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP002I001, list_TLDP002I002):
            t_time = timeCaculation(tLDP001,tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('ZIPファイル展開   ',str(tLDP001[1]),str(tLDP002[1]),str(t_time)))
###TLDP002I001   ZIP展開


###TLDP003I001  ファイル変換1
    # ファイル変換開始Index
    list_TLDP003I001_p1 = list(filter(lambda x: (x[0]=='TLDP003I001') and ('Process1' in x[2]), line))
    if len(list_TLDP003I001_p1) > 0:
        tLDP003_FirstAppearIndex = line.index(list_TLDP003I001_p1[0])
        list_TLDP003I002_p1 = list(filter(lambda x:(x[0]=='TLDP003I002') and ('Process1' in x[2]), line[tLDP003_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP003I001_p1, list_TLDP003I002_p1):
            t_time = timeCaculation(tLDP001,tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('ファイル変換      ',str(tLDP001[1]),str(tLDP002[1]),str(t_time)))
###TLDP003I001 ファイル変換1

###TLDP003I001  ファイル変換2
        # ファイル変換開始Index
    list_TLDP003I001_p2 = list(filter(lambda x: (x[0] == 'TLDP003I001') and ('Process2' in x[2]), line))
    if len(list_TLDP003I001_p2) > 0:
        tLDP003_FirstAppearIndex = line.index(list_TLDP003I001_p2[0])
        list_TLDP003I002_p2 = list(filter(lambda x: (x[0] == 'TLDP003I002') and ('Process2' in x[2]), line[tLDP003_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP003I001_p2, list_TLDP003I002_p2):
            t_time = timeCaculation(tLDP001, tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('ファイル変換      ', str(tLDP001[1]), str(tLDP002[1]), str(t_time)))
###TLDP003I001 ファイル変換2


###TLDP004I001 JoinTSV
    list_TLDP004I001= list(filter(lambda x: x[0]=='TLDP004I001', line))
    if len(list_TLDP004I001) > 0:
        tLDP004_FirstAppearIndex = line.index(list_TLDP004I001[0])
        # TLDP004I001がはじめ出た行の以後から、TLDP002I002を収集
        list_TLDP004I002 = list(filter(lambda x: x[0]=='TLDP004I002', line[tLDP004_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP004I001, list_TLDP004I002):
            t_time = timeCaculation(tLDP001,tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('可読化ファイル結合', str(tLDP001[1]), str(tLDP002[1]), str(t_time)))

###TLDP004I001 JoinTSV

###TLDP005I001 HDFS連携
    list_TLDP005I001= list(filter(lambda x: x[0]=='TLDP005I001', line))
    if len(list_TLDP005I001) > 0:
        tLDP005_FirstAppearIndex = line.index(list_TLDP005I001[0])
        # TLDP005I001がはじめ出た行の以後から、TLDP005I002を収集
        list_TLDP005I002 = list(filter(lambda x:  x[0]=='TLDP005I002', line[tLDP005_FirstAppearIndex:]))
        for tLDP001, tLDP002 in zip(list_TLDP005I001, list_TLDP005I002):
            t_time = timeCaculation(tLDP001,tLDP002)
            OutputList.append('{0},{1},{2},{3}'.format('可読化ファイル連携', str(tLDP001[1]), str(tLDP002[1]), str(t_time)))

###TLDP005I001 HDFS連携

#OutLog
    if len(OutputList)>0:
        logName = fileType+'_'+analyze_datetime+'.log'
        with open(out_path + logName, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + newLineCode)


def create_Pic(fileType,analyze_datetime):
    jobtype=('ZIP取り込み       ','ZIPファイル展開   ','ファイル変換      ','可読化ファイル結合','可読化ファイル連携')
    jobtype_Name=('getZIP','extractZIP','transformFile','joinFile','sendToHdfs')
    logName = fileType+'_'+analyze_datetime+'.log'
    if os.path.isfile(out_path + logName):
        fileinfo = pd.read_csv(out_path + logName, sep=',', encoding="utf_8", names=["type", "start", "end", "due"])
    else:
        return
    for jobCount in range(5):
        jobinfo = fileinfo[fileinfo["type"] == jobtype[jobCount]]
        jobinfo = jobinfo[jobinfo["due"] > 2.0]
        jobinfo = jobinfo[jobinfo["due"] < 300.0]
        if jobinfo.empty:
            continue

        # Get max min average value
        during_time = jobinfo['due'].tolist()
        max_value = max(during_time)
        min_value = min(during_time)
        avr_value = sum(during_time) / len(during_time)
        statistic_path = pic_path+'ProbeJob_Statistic.txt'
        with open(statistic_path, "a+", encoding='utf-8') as file:
            file.write(fileType +'   '+analyze_datetime+'['+str.strip(jobtype[jobCount])+']'+'実行時間統計' + newLineCode)
            file.write('    最大実行時間：'+str(max_value)+ newLineCode)
            file.write('    最小実行時間：' + str(min_value)+ newLineCode)
            file.write('    平均実行時間：' + str(min_value)+ newLineCode)

        jobinfo["due"].plot(kind='kde')
        pyplot.grid(True)
        pyplot.text(5, 5, jobinfo.describe())
        pyplot.xlim(0, 100)
        pic_name=fileType+'_'+jobtype_Name[jobCount]+'_pic.png'
        pyplot.savefig(pic_path+pic_name)
        pyplot.close()

def timeCaculation(list_s, list_e):
    return (list_e[1]-list_s[1]).seconds


