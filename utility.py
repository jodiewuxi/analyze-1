import datetime
out_path = "D:\LocalData\FJT02454\Desktop\logAnalyze"
seperateStr=','

def logAnalyze(fileType,line ,analyze_datetime):
    OutputList=[]
###TLDP001I001  ZIP 取り込み
    list_TLDP001I001= list(filter(lambda x: 'TLDP001I001' in x, line))
    tLDP001_FirstAppearIndex = getFirstAppearIndex('TLDP001I001',line)

    # TLDP001I001がはじめ出た行の以後から、TLDP001I002を収集
    list_TLDP001I002 = list(filter(lambda x: 'TLDP001I002' in x, line[tLDP001_FirstAppearIndex:]))
    for tLDP001, tLDP002 in zip(list_TLDP001I001, list_TLDP001I002):
        t_time = timeText(tLDP001,tLDP002)
        OutputList.append('ZIP取り込み       '+seperateStr + t_time)
###TLDP001I001  ZIP 取り込み

###TLDP002I001  ZIP展開
    list_TLDP002I001= list(filter(lambda x: 'TLDP002I001' in x, line))
    tLDP002_FirstAppearIndex = getFirstAppearIndex('TLDP002I001',line)

    # TLDP002I001がはじめ出た行の以後から、TLDP002I002を収集
    list_TLDP002I002 = list(filter(lambda x: 'TLDP002I002' in x, line[tLDP002_FirstAppearIndex:]))
    for tLDP001, tLDP002 in zip(list_TLDP002I001, list_TLDP002I002):
        t_time = timeText(tLDP001,tLDP002)
        OutputList.append('ZIPファイル展開   '+ seperateStr + t_time)
###TLDP002I001   ZIP展開


###TLDP003I001  ファイル変換
    # ZIP取り込み開始Index
    getZIPJOB_AppearIndex = getFirstAppearIndex('TLDP001I001',line)

    # ファイル変換開始Index
    tLDP003_FirstAppearIndex = getFirstAppearIndex('TLDP003I001', line[getZIPJOB_AppearIndex:])

    list_TLDP003I001= list(filter(lambda x: 'TLDP003I001' in x, line[getZIPJOB_AppearIndex:]))
    list_TLDP003I002 = list(filter(lambda x: 'TLDP003I002' in x, line[(getZIPJOB_AppearIndex+tLDP003_FirstAppearIndex):]))

    paralleNo = 0
    tLDP001_s=[]
    tLDP001_e=[]
    for tLDP001, tLDP002 in zip(list_TLDP003I001, list_TLDP003I002):
        paralleNo += 1
        tLDP001_s.append(tLDP001)       #start 控え
        tLDP001_e.append(tLDP002)       #end  控え
        if paralleNo==2:
            t_time = timeText(getEarlyStarttime(tLDP001_s),getSlowEndTime(tLDP001_e))
            OutputList.append('ファイル変換      ' + seperateStr + t_time)
            paralleNo = 0
            tLDP001_s = []
            tLDP001_e = []
###TLDP003I001 ファイル変換

###TLDP004I001 JoinTSV
    list_TLDP004I001= list(filter(lambda x: 'TLDP004I001' in x, line))

    tLDP004_FirstAppearIndex = getFirstAppearIndex('TLDP004I001',line)

    # TLDP004I001がはじめ出た行の以後から、TLDP004I002を収集
    list_TLDP004I002 = list(filter(lambda x: 'TLDP004I002' in x, line[tLDP004_FirstAppearIndex:]))
    for tLDP001, tLDP002 in zip(list_TLDP004I001, list_TLDP004I002):
        t_time = timeText(tLDP001,tLDP002)
        OutputList.append('可読化ファイル結合'+ seperateStr +t_time)

###TLDP004I001 JoinTSV

###TLDP005I001 HDFS連携
    list_TLDP005I001= list(filter(lambda x: 'TLDP005I001' in x, line))
    tLDP005_FirstAppearIndex = getFirstAppearIndex('TLDP005I001',line)

    # TLDP005I001がはじめ出た行の以後から、TLDP005I002を収集
    list_TLDP005I002 = list(filter(lambda x: 'TLDP005I002' in x, line[tLDP005_FirstAppearIndex:]))
    for tLDP001, tLDP002 in zip(list_TLDP005I001, list_TLDP005I002):
        t_time = timeText(tLDP001,tLDP002)
        OutputList.append('可読化ファイル連携'+ seperateStr +t_time)

###TLDP005I001 HDFS連携

#OutLog
    if fileType == 'CW':
        cw_logName = '\\CW_'+analyze_datetime+'.log'
        with open(out_path + cw_logName, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'GEN1':
        gen1_logName = '\\GEN1_' + analyze_datetime + '.log'
        with open(out_path + gen1_logName, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'GEN2':
        gen2_logName = '\\GEN2_' + analyze_datetime + '.log'
        with open(out_path + gen2_logName, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'SXM':
        sxm_logName = '\\SXM_' + analyze_datetime + '.log'
        with open(out_path + sxm_logName, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")



#local function

def getSlowEndTime(timeList):
    list1 = timeList[0].split()
    list2 = timeList[1].split()
    tdatetime_S1 = datetime.datetime.strptime(list1[4] + ' ' + list1[5], '%Y%m%d %H%M%S')
    tdatetime_S2 = datetime.datetime.strptime(list2[4] + ' ' + list2[5], '%Y%m%d %H%M%S')
    if (tdatetime_S1 > tdatetime_S2):
        e_str = timeList[0]
    else:
        e_str = timeList[1]
    return e_str

def getEarlyStarttime(timeList):
    list1 = timeList[0].split()
    list2 = timeList[1].split()
    tdatetime_S1 = datetime.datetime.strptime(list1[4] + ' ' + list1[5], '%Y%m%d %H%M%S')
    tdatetime_S2 = datetime.datetime.strptime(list2[4] + ' ' + list2[5], '%Y%m%d %H%M%S')

    if (tdatetime_S1 > tdatetime_S2):
        s_str = timeList[1]
    else:
        s_str = timeList[0]

    return s_str


def getFirstAppearIndex(value,line):
    index_value=0
    for ln in line:
        if value in ln:
            index_value=line.index(ln)
            break
    return index_value

def timeText(list_s,list_e):
    startDate= (list_s.split())[4]
    startTime= (list_s.split())[5]
    endDate= (list_e.split())[4]
    endTime= (list_e.split())[5]
    start_end_duringTime = timeCaculation(startDate,startTime,endDate,endTime)
    return start_end_duringTime

def timeCaculation(startDate, startTime, endDate, endTime):
    tdatetime_S = datetime.datetime.strptime(startDate+' '+startTime, '%Y%m%d %H%M%S')
    tdatetime_E = datetime.datetime.strptime(endDate+' '+endTime, '%Y%m%d %H%M%S')
    return str(tdatetime_S)+ seperateStr +str(tdatetime_E)+ seperateStr +str(tdatetime_E - tdatetime_S)

def debugPrint(list):
        for ls in list:
            print(ls)

