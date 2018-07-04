import utility_new
import sys
import datetime
import os
import fnmatch

log_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze"
#log_file_path = r"/Teclog"

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
    cwline = []
    gen1line = []
    gen2line = []
    sxmline = []
    # get logfile list
    for file in os.listdir(log_file_path):
        if fnmatch.fnmatch(file, 'Applinfo.log.[1-9]') or file=='Applinfo.log':
            print(file)
            # open log file
            with open(log_file_path + '\\' + file, "r", encoding='utf-8') as file:
                data = file.read()
                logline = data.split('\n')
            # open log file
            cwline.extend(list(filter(lambda x: ('CW ' + log_time) in x, logline)))
            gen1line.extend(list(filter(lambda x: ('GEN1 ' + log_time) in x, logline)))
            gen2line.extend(list(filter(lambda x: ('GEN2 ' + log_time) in x, logline)))
            sxmline.extend(list(filter(lambda x: ('SXM ' + log_time) in x, logline)))
        # Split line
    sortcwline = splitSort(cwline)
    sortgen1line = splitSort(gen1line)
    sortgen2line = splitSort(gen2line)
    sortsxmline = splitSort(sxmline)

    utility_new.logAnalyze('CW', sortcwline, log_time)
    utility_new.logAnalyze('GEN1', sortgen1line, log_time)
    utility_new.logAnalyze('GEN2', sortgen2line, log_time)
    utility_new.logAnalyze('SXM', sortsxmline, log_time)
    print(log_time + 'のLogを出力しました。')

if __name__ == '__main__':
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
