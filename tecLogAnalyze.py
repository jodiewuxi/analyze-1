import utility
import sys
import datetime

log_file_path = r"D:\LocalData\FJT02454\Desktop\logAnalyze\Applinfo.log"


def checkDate(dateStr):
    try:
        newDate=datetime.datetime.strptime(dateStr,"%Y%m%d")
        return True
    except ValueError:
        return False



def main(log_time):
#変数定義
    logline = []
    cwline = []
    gen1line=[]
    gen2line=[]
    sxmline=[]
    otherine=[]
#変数定義

#open log file
    with open(log_file_path, "r", encoding='utf-8') as file:
        data = file.read()
        logline = data.split('\n')
#open log file

    cwline = list(filter(lambda x: ('CW '+log_time) in x, logline))
    gen1line = list(filter(lambda x: ('GEN1 '+log_time) in x, logline))
    gen2line = list(filter(lambda x: ('GEN2 '+log_time) in x, logline))
    sxmline = list(filter(lambda x: ('SXM ' + log_time) in x, logline))

    utility.logAnalyze('CW', cwline, log_time)
    utility.logAnalyze('GEN1', gen1line, log_time)
    utility.logAnalyze('GEN2', gen2line, log_time)
    utility.logAnalyze('SXM', sxmline, log_time)

    print(log_time+'のLogを出力しました。')

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
