import requests
from bs4 import BeautifulSoup
url = ('https://www.jobui.com/rank/company/guangzhou/')

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res = requests.get(url,headers = headers)

print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')

parts = soup.find_all(class_ = 'textList flsty cfix')

list = []
for part in parts:
    namea = part.find_all('a')
    for i in range(5):
        nameb = namea[i].text
        list.append(nameb)
print(list)