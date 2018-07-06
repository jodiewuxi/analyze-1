import json

tx=open(r'D:\LocalData\FJT02454\Documents\mywork\Probe\Vnext\mergeddata.json')
js=json.load(tx)

record_1=js[0]
record_1_data=record_1["dataFields"]

print(record_1_data)