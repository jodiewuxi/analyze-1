import datetime
cw_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\\CW.log"
gen1_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\\GEN1.log"
gen2_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\\GEN2.log"
sxm_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\\SXM.log"

OutputList=[]
processlist = []


def paralleProcesstimeCaculation(timeList):
    list1 = timeList[0].split()
    list2 = timeList[1].split()

    ps1StartDate = list1[1]
    ps1StartTime = list1[2]

    ps1Startyear = ps1StartDate[0:4]
    ps1Startmonth = ps1StartDate[4:6]
    ps1Startday = ps1StartDate[6:8]
    ps1Starthour = ps1StartTime[0:2]
    ps1Startminute = ps1StartTime[2:4]
    ps1Startsecond = ps1StartTime[4:6]

    ps1EndDate = list1[3]
    ps1EndTime = list1[4]

    ps1Endyear = ps1EndDate[0:4]
    ps1Endmonth = ps1EndDate[4:6]
    ps1Endday = ps1EndDate[6:8]
    ps1Endhour = ps1EndTime[0:2]
    ps1Endminute = ps1EndTime[2:4]
    ps1Endsecond = ps1EndTime[4:6]

    ps2StartDate = list2[1]
    ps2StartTime = list2[2]

    ps2Startyear = ps2StartDate[0:4]
    ps2Startmonth = ps2StartDate[4:6]
    ps2Startday = ps2StartDate[6:8]
    ps2Starthour = ps2StartTime[0:2]
    ps2Startminute = ps2StartTime[2:4]
    ps2Startsecond = ps2StartTime[4:6]

    ps2EndDate = list2[3]
    ps2EndTime = list2[4]

    ps2Endyear = ps2EndDate[0:4]
    ps2Endmonth = ps2EndDate[4:6]
    ps2Endday = ps2EndDate[6:8]
    ps2Endhour = ps2EndTime[0:2]
    ps2Endminute = ps2EndTime[2:4]
    ps2Endsecond = ps2EndTime[4:6]

    ps1StartDatetime = datetime.datetime(int(ps1Startyear), int(ps1Startmonth), int(ps1Startday), int(ps1Starthour),
                                         int(ps1Startminute), int(ps1Startsecond))
    ps1EndDatetime = datetime.datetime(int(ps1Endyear), int(ps1Endmonth), int(ps1Endday), int(ps1Endhour),
                                       int(ps1Endminute), int(ps1Endsecond))

    ps2StartDatetime = datetime.datetime(int(ps2Startyear), int(ps2Startmonth), int(ps2Startday), int(ps2Starthour),
                                         int(ps2Startminute), int(ps2Startsecond))
    ps2EndDatetime = datetime.datetime(int(ps2Endyear), int(ps2Endmonth), int(ps2Endday), int(ps2Endhour),
                                       int(ps2Endminute), int(ps2Endsecond))

    if (ps1StartDatetime > ps2StartDatetime):
        startDate = ps2StartDate
        startTime = ps2StartTime
        startDateTime = ps2StartDatetime
    else:
        startDate = ps1StartDate
        startTime = ps1StartTime
        startDateTime = ps1StartDatetime

    if (ps1EndDatetime > ps2EndDatetime):
        endDate= ps1EndDate
        endTime=ps1EndTime
        endDateTime = ps1EndDatetime
    else:
        endDate= ps2EndDate
        endTime=ps2EndTime
        endDateTime = ps2EndDatetime

    return 'ファイル変換      '+' '+startDate + ' '+startTime+' '+endDate+' '+endTime+' '+str(endDateTime-startDateTime)


def timeCaculation(startDate, startTime, endDate, endTime):
    year1 = startDate[0:4]
    month1 = startDate[4:6]
    day1 = startDate[6:8]
    hour1 = startTime[0:2]
    minute1 = startTime[2:4]
    second1 = startTime[4:6]

    year2 = endDate[0:4]
    month2 = endDate[4:6]
    day2 = endDate[6:8]
    hour2 = endTime[0:2]
    minute2 = endTime[2:4]
    second2 = endTime[4:6]

    d1 = datetime.datetime(int(year1), int(month1), int(day1), int(hour1), int(minute1), int(second1))
    d2 = datetime.datetime(int(year2), int(month2), int(day2), int(hour2), int(minute2), int(second2))
    return str(d2 - d1)

def logAnalyze(fileType,line):
    for i in range(0,len(line)):
        print(line[i])
        if line[i] != []:
            fieldlist=line[i].split()

            if fieldlist[0] == 'TLDP001I001':
                for j in range(i+1,len(line)):
                    if line[j] != []:
                        fieldlist1 = line[j].split()
                        if fieldlist1[0] == 'TLDP001I002':  # getzip end
                            durationTime=timeCaculation(fieldlist[4],fieldlist[5],fieldlist1[4],fieldlist1[5])
                            outPutText = 'ZIP取り込み       ' + ' ' + fieldlist[4] + ' ' + fieldlist[5]+' ' + fieldlist1[4]+' '+fieldlist1[5]+' '+durationTime
                            OutputList.append(outPutText)
                            break
            elif fieldlist[0] == 'TLDP002I001':  # extract start
                for j in range(i+1,len(line)):
                    if line[j] != []:
                        fieldlist1 = line[j].split()
                        if fieldlist1[0] == 'TLDP002I002':  # extract end
                            durationTime = timeCaculation(fieldlist[4], fieldlist[5], fieldlist1[4], fieldlist1[5])
                            outPutText = 'ZIPファイル展開   ' + ' ' + fieldlist[4] + ' ' + fieldlist[5]+' ' + fieldlist1[4]+' '+fieldlist1[5]+' '+durationTime
                            OutputList.append(outPutText)
                            break
            elif fieldlist[0] == 'TLDP003I001':  # transfrom start
                if fieldlist[8].find('Process1')>-1:    #transfrom1 Start
                    for j in range(i + 1, len(line)):
                        if line[j] != []:
                            fieldlist1 = line[j].split()
                            if fieldlist1[0] == 'TLDP003I002':  #transform end
                                if fieldlist1[8].find('Process1') > -1:
                                     outPutText = 'ファイル変換1' + ' ' + fieldlist[4] + ' ' + fieldlist[5] + ' ' + fieldlist1[4] + ' ' + fieldlist1[5]
                                     processlist.append(outPutText)
                                     break

                    #pslist.append(line[i])
                elif fieldlist[8].find('Process2')>-1:  #transform2 start
                    for j in range(i + 1, len(line)):
                        if line[j] != []:
                            fieldlist1 = line[j].split()
                            if fieldlist1[0] == 'TLDP003I002':  # transform2 end
                                if fieldlist1[8].find('Process2') > -1:
                                    outPutText = 'ファイル変換2' + ' ' + fieldlist[4] + ' ' + fieldlist[5] + ' ' + fieldlist1[4] + ' ' + fieldlist1[5]
                                    if len(processlist) == 1:
                                        processlist.append(outPutText)
                                        processLog = paralleProcesstimeCaculation(processlist)
                                        OutputList.append(processLog)
                                        processlist[:]=[]
                                    break
            elif fieldlist[0] == 'TLDP004I001':  # jointsv
                for j in range(i+1,len(line)):
                    if line[j] != []:
                        fieldlist1 = line[j].split()
                        if fieldlist1[0] == 'TLDP004I002':  # jointsv end
                            durationTime = timeCaculation(fieldlist[4], fieldlist[5], fieldlist1[4], fieldlist1[5])  #処理時間
                            outPutText = '可読化ファイル結合' + ' ' + fieldlist[4] + ' ' + fieldlist[5]+' ' + fieldlist1[4]+' '+fieldlist1[5]+' '+durationTime
                            OutputList.append(outPutText)
                            break
            elif fieldlist[0] == 'TLDP005I001':  # send to hdfs
                for j in range(i+1,len(line)-1): # find end signal from next line
                    if line[j] != []:
                        fieldlist1 = line[j].split()
                        if fieldlist1[0] == 'TLDP005I002':  # send to hdfs end
                            durationTime = timeCaculation(fieldlist[4], fieldlist[5], fieldlist1[4], fieldlist1[5])  #処理時間
                            outPutText = '可読化ファイル連携' + ' ' + fieldlist[4] + ' ' + fieldlist[5]+' ' + fieldlist1[4]+' '+fieldlist1[5]+' '+durationTime
                            OutputList.append(outPutText)
                            break
    if fileType == 'CW':
        with open(cw_file_path, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'GEN1':
        with open(gen1_file_path, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'GEN2':
        with open(gen2_file_path, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")
    elif fileType == 'SXM':
        with open(sxm_file_path, "w+", encoding='utf-8') as file:
            for ls in OutputList:
                file.write(ls + "\n")