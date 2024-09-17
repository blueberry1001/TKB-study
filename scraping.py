import html_get
import json
from datetime import datetime
import urllib.parse
#getdataする


baseurl = "https://scrapbox.io/Atcoder-myReflection/"
#いったん10ページ取得しよう
urllist = html_get.gethtml("https://scrapbox.io/api/pages/Atcoder-myReflection?limit=1000")
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
    for line in page_text.splitlines():
        # 問題が始まったら打ち切り
        if "[**% 問題]" in line:
            break
        # タグの抽出
        line_tags = [i for i in line.split() if i[0] == "#"]
        tags += line_tags
        # Difficultyの抽出
        if line.startswith("Difficulty:"):
            diff = line.lstrip("Difficulty:")
            try:
                diff = int(diff)
            except ValueError:
                pass
    if diff is not None:
        resdic[pagename] = {"Difficulty": diff, "Tags": tags}
        print(pagename, diff, tags)

now = datetime.now().strftime(r"%Y%m%d_%H%M%S")

with open(f"data_{now}.json", 'w') as f:
    json.dump(resdic, f, indent=2)