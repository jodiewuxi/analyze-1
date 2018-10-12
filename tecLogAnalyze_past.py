import utility_new_ver1
import sys
import datetime
import os
import fnmatch

log_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\\"
#log_file_path = r"/Teclog/"

def checkDate(dateStr):
    try:
        newDate=datetime.datetime.strptime(dateStr,"%Y%m%d")
        return True
    except ValueError:
        return False

def datetimeTransfer(s_Date, s_Time):
    tdatetime_S = datetime.datetime.strptime(s_Date + ' ' + s_Time, '%Y%m%d %H%M%S')
    return tdatetime_S


def splitSort(filelist):
    filelist_new = []
    for ls in filelist:
        list_tmp=[]
        filelist_split = ls.split()
        # Transfer String into DateTime
        date_time = datetimeTransfer(filelist_split[4], filelist_split[5])
        list_tmp.append(filelist_split[0])
        list_tmp.append(date_time)
        list_tmp.append(filelist_split[8])
        filelist_new.append(list_tmp)
    return sorted(filelist_new, key=lambda x: x[1])



def main(log_time):
    now_cwline = []
    now_gen1line = []
    now_gen2line = []
    now_sxmline = []
    now_gen2kline = []

    past_cwline = []
    past_gen1line = []
    past_gen2line = []
    past_sxmline = []
    past_gen2kline = []


    # get logfile list
    for file in os.listdir(log_file_path):
        if fnmatch.fnmatch(file, 'Applinfo.log.[1-9]') or file=='Applinfo.log':
            # open log file
            with open(log_file_path + file, "r", encoding='utf-8') as file:
                data = file.read()
                logline = data.split('\n')
            # open log file
            past_cwline.extend(list(filter(lambda x: ('TLDP002 CW ' + log_time) in x, logline)))
            past_gen1line.extend(list(filter(lambda x: ('TLDP002 GEN1 ' + log_time) in x, logline)))
            past_gen2line.extend(list(filter(lambda x: ('TLDP002 GEN2 ' + log_time) in x, logline)))
            past_sxmline.extend(list(filter(lambda x: ('TLDP002 SXM ' + log_time) in x, logline)))
            past_gen2kline.extend(list(filter(lambda x: ('TLDP002 GEN2K ' + log_time) in x, logline)))
        # Split line
    sortcwline = splitSort(past_cwline)
    sortgen1line = splitSort(past_gen1line)
    sortgen2line = splitSort(past_gen2line)
    sortsxmline = splitSort(past_sxmline)
    sortgen2kline = splitSort(past_gen2kline)

    utility_new_ver1.logAnalyze('CW', sortcwline, log_time)
    utility_new_ver1.logAnalyze('GEN1', sortgen1line, log_time)
    utility_new_ver1.logAnalyze('GEN2', sortgen2line, log_time)
    utility_new_ver1.logAnalyze('GEN2K', sortgen2kline, log_time)
    utility_new_ver1.logAnalyze('SXM', sortsxmline, log_time)

    #Pic作成
    #utility_new_ver1.create_Pic('CW',log_time)
    #utility_new_ver1.create_Pic('GEN1',log_time)
    #utility_new_ver1.create_Pic('GEN2', log_time)
    #utility_new_ver1.create_Pic('GEN2K', log_time)
    #utility_new_ver1.create_Pic('SXM', log_time)

    print(log_time + 'のLogを出力しました。')

if __name__ == '__main__':
    main('20181012')
'''
    args = sys.argv
    if len(args)>=2:
        if len(args[1]) != 8:
            print('以下のように日付を指定してください')
            print('YYYYMMDD')
            quit()
        else:
            if checkDate(args[1]):

                main(args[1])

            else:
                print('日付は間違いました。以下のように指定してください')
                print('YYYYMMDD')
                quit()
    else:
        print('以下のように日付を指定してください')
        print('YYYYMMDD')
        quit()
'''