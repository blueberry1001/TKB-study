#モジュールのインポート
import urllib.request
from bs4 import BeautifulSoup

#対象のサイトURL
url = "https://www2.nhk.or.jp/archives/movies/?id=D0001300386_00000&chapter=002"

#URLリソースを開く
res = urllib.request.urlopen(url)
print(res)
#インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

#必要な要素とclass名
name = soup.find_all(class_="chapter-text")

#取得したタイトル情報を出力
ret = []
for t in name:
    ret.append(t.text)

print(ret)
