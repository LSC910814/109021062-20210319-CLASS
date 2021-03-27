import requests as reqs
from bs4 import BeautifulSoup

req=reqs.get(
    "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding="big5"
if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("p")
    fp = open("huang.txt", "w", encoding="utf8")
    for val in result1:
        text2 = val.text.replace('\n', '')
        text3 = text2.replace('  ','')
        print(text3)
        fp.write(text3+"\n")
    fp.close()
else:
    print("no page")