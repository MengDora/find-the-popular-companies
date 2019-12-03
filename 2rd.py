import requests
from bs4 import BeautifulSoup
Url = ('https://www.jobui.com/rank/company/guangzhou/')

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res = requests.get(Url,headers = headers)

print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')

parts = soup.find_all(class_ = 'textList flsty cfix')

list = []

for part in parts:
    namea = part.find_all('a')
    item = []
    for i in namea:
        nameb = i.text
        urls = i['href']
        url1 = 'https://www.jobui.com{x}jobs'
        url2 = url1.format(x = urls)
        item.append(nameb + '----' + '网址:' + '----' + url2)
        #item.append()
        list.append(item)

print(list)