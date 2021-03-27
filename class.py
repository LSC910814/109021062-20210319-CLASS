import requests as reqs
from bs4 import BeautifulSoup

req=reqs.get(
    "https://www.intechopen.com/books/bioinformatics-in-the-era-of-post-genomics-and-big-data/a-novel-approach-to-mine-for-genetic-markers-via-comparing-class-frequency-distributions-of-maximal-")
req.encoding="utf8"
if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("li")
    fp = open("out2.txt", "w", encoding="utf8")
    for val in result1:
        text2 = val.text.replace('\n', '')
        text3 = text2.replace('  ','')
        print(text3)
        fp.write(text3+"\n")
    fp.close()

else:
    print("no page")