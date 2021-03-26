import requests as reqs
from bs4 import BeautifulSoup

req=reqs.get(
    "http://120.108.116.237/~jackjow/pubList.php")
req.encoding="utf8"
if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text, "lxml")
    print(soup)
    result1 = soup.find("li")
    print(result1)
else:
    print("no page")