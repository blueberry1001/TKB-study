import json
import pandas as pd
url = "https://atcoder.jp/contests/dp/tasks/dp_z"
with open('model_20241125_055221.json', 'r', encoding='utf-8') as file:
    model = json.load(file)

import html_get
words = html_get.getdata(url)
ret = dict()
for word in words:
    print(word)
    if word not in model:
        print("Word not found")
        continue
    for i in model[word]:
        if i not in ret:
            ret[i] = 0
        ret[i]+=model[word][i]
#値が高いもの順にソート
sortedret = sorted(ret.items(),key=lambda item:item[1],reverse=True)
for i,j in sortedret:
    print(i,j)