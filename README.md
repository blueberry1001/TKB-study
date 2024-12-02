# TKB-study
筑波スタディのリポジトリ。

## 概要
競技プログラミングについての研究をしている。問題文と解法をペアにしたものをデータとして学習し、新しく問題文が与えられた際にその問題がどのような解法で解くことができそうかを予測する。

### html_get.py
htmlに関するコード。
#### gethtml(url:str)
URLに対してGETリクエストを送り、帰ってきたHTMLデータをstr形式で得る。
#### get_problemstatement(s:str)
与えられた文字列のうち、問題文の部分を抜き出す。
#### getdata(url:str)
引数に渡された問題URLの問題文をtokenizeして返す。

### scraping.py
スクレイピングをする。
Scrapboxのデータをもとに、問題をキー、(Difficulty,タグ,問題URL,問題文に含まれる単語)を要素として持つdictをつくり、data_日時.jsonとして保存する。
### main.py
ある問題に対して、類似する問題についているタグを列挙する。