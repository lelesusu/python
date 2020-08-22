import requests
from bs4 import BeautifulSoup

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
for x in range(3):
    params = {
    'g_tk_new_20200303': '1161943071',
    'g_tk': '1161943071',
    'loginUin': '1208046901',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '102065756',
    'cmd': '8',
    'needmusiccrit': '0',
    'pagenum': str(x),
    'pagesize': '25',
    'lasthotcommentid': 'song_102065756_1152921504960203409_1598076579',
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010'
    }
    res = requests.get(url,params=params)
    comment = res.json()
    list_comment = comment['comment']['commentlist']
    for i in list_comment:
        print('\n')
        print(i['rootcommentcontent'])