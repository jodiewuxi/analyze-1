import pandas as pd
import matplotlib.pyplot as plt
gen2df = pd.read_csv("D:\LocalData\FJT02454\Desktop\logAnalyze\GEN1_20180622.log", sep=',', encoding="utf_8", names=["type", "start", "end", "due"])
gen2df = gen2df[gen2df["type"] == "可読化ファイル連携"]
gen2df = gen2df[gen2df["due"] > 2.0]
gen2cvn = gen2df[gen2df["due"] < 300.0]
#gen2cvn = pd.to_datetime(gen2cvn['due'])
print(gen2cvn.describe())
if gen2cvn.empty:
    exit()
gen2cvn["due"].plot(kind='kde')
plt.grid(True)
plt.text(5, 5, gen2cvn.describe())
plt.xlim(0, 100)
plt.show() 
