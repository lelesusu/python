import requests
from bs4 import BeautifulSoup
url = 'http://www.chinaygj.com/index.php'
for x in range(8):
    params = {
    'm': 'content',
    'c': 'index',
    'a': 'lists',
    'catid': '232',       #直接改动这里可以爬取到另一个栏目里的内容，如233代表最佳实践栏目，232代表产品优惠栏目
    'page': str(x+1)
    }
    res = requests.get(url,params=params)
    name = BeautifulSoup(res.text,'html.parser')
    name_list = name.find('ul',class_='zx-list',id="DataUl")  
    list2 = name_list.find_all('div',class_='zx-list-tt')     #最小的标签包含了不需要的东西，就要先find，再find_all
    for i in list2:
        print(i.text)