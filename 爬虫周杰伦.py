import requests
from bs4 import BeautifulSoup

res = requests.get(r'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61234074649777090&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
music = res.json()
list_music = music['data']['song']['list']
for i in list_music:
    print('\n\n')
    print(i['name'])
    print('所属专辑：'+i['album']['name'])
    print('发行时间：'+i['time_public'])
    print('链接：'+i['url'])
    print('链接：'+i['url2'])
    print('链接：'+i['url2'])
    # print(type(i['time_public']))
    # print(type(i['name']))