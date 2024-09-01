import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.goodead.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels')
print(page.status_code)
soup=BeautifulSoup(page.content,'html.parser')
titles=soup.select('.tableList tr[itemtype="http://schema.org/Book"] a.booTitle span[itemprop="name"]')
first10=titles[:10]
for anchor in first10:
    print(anchor.text)