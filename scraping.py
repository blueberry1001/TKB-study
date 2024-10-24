import html_get
import json
from datetime import datetime
import urllib.parse
#getdataする


baseurl = "https://scrapbox.io/Atcoder-myReflection/"
#いったん10ページ取得しよう
urllist = html_get.gethtml("https://scrapbox.io/api/pages/Atcoder-myReflection?limit=1000")
test = True
if test:
    urllist = html_get.gethtml("https://scrapbox.io/api/pages/Atcoder-myReflection?limit=10")
pagelist = json.loads(urllist)
resdic = dict()

for article in pagelist["pages"]:
    pagename = urllib.parse.quote(article["title"].replace(" ","_"))
    page_text = html_get.gethtml("https://scrapbox.io/api/pages/Atcoder-myReflection/"+pagename+"/text")
    if page_text is None:
        continue
    tags = []
    diff: int | None = None
    problem_url = ""
    next_is_url:bool = False
    for line in page_text.splitlines():
        # 問題が始まったら打ち切り
        if "[**% 問題]" in line:
            break
        # タグの抽出
        line_tags = [i for i in line.split() if i[0] == "#"]
        tags += line_tags
        # 問題リンクの取得
        if next_is_url:
            problem_url = line[1:-5]
            next_is_url = False
        # Difficultyの抽出
        if line.startswith("Difficulty:"):
            next_is_url = True
            diff = line.lstrip("Difficulty:")
            try:
                diff = int(diff)
            except ValueError:
                pass
    if diff is not None:
        resdic[pagename] = {
            "Difficulty": diff,
            "Tags": tags,
            "URL": problem_url
        }
        print(pagename, diff, tags)

now = datetime.now().strftime(r"%Y%m%d_%H%M%S")

with open(f"data_{now}.json", 'w') as f:
    json.dump(resdic, f, indent=2)