import requests
from bs4 import BeautifulSoup

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection':'Keep-Alive',
               'Host':'www.xiachufang.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(r'http://www.xiachufang.com/explore/', headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
soup_list = soup.find_all('div',class_='info pure-u')
for i in soup_list:
    kind = i.find('p', class_='name')
    print(kind.text)