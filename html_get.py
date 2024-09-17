import requests
import re
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

def gethtml(url):
    response = requests.get(url)
    ret = None
    if response.status_code == 200:
        ret = response.text
    else:
        print(url, response.status_code, response.json())
    return ret

def get_problemstatement(s):
    #"<section><h3>問題文</h3>"から"</section>"まで
    ret = ""
    now = 0
    fir = "<section><h3>問題文</h3>"
    end = "</section>"
    pos = 0
    for i in s:
        if now == 0:
            if fir[pos]==i:
                pos+=1
            if pos == len(fir):
                now += 1
                pos = 0
        elif now == 1:
            ret += i
            if end[pos]==i:
                pos+=1
            if pos == len(end):
                now += 1
                pos = 0
        else:
            break
    return "<section>" + ret + end

def getdata(url = ""):
    html_d = gethtml(url)
    ret = get_problemstatement(html_d)
    soup = BeautifulSoup(ret, 'html.parser')
    tag = soup.select("section")[0].get_text()
    problemstatement =  tag.replace(" ","").replace("　","")

    t = Tokenizer(wakati=True)
    ret = t.tokenize(problemstatement)
    for token in t.tokenize(problemstatement):
        print(token)
    ret = list(ret)
    # print(ret)
    ret = sorted(set(ret),reverse=True)
    return ret
# print(getdata("https://atcoder.jp/contests/abc361/tasks/abc361_a"))