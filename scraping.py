import html_get
#getdataする



baseurl = "https://scrapbox.io/Atcoder-myReflection/"
urllist = html_get.gethtml("https://scrapbox.io/api/pages/Atcoder-myReflection")
print(urllist)