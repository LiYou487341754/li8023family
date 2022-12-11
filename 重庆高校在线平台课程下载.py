# 重庆高校课程下载
import os
import requests


name = 'ps视频'
if not os.path.exists(name):
    os.mkdir(name)
xsid = input("请输入xsid:")
sign_url = 'https://www.cqooc.com/user/session?xsid=' + xsid
session = requests.Session()
headers = {
    'Cookie': '_abfpc=39fe931bb4d61da3ebe1ef4b5a75f1a0ac8f654b_2.0; '
              'cna=788491930f78f10d984ec4c628aeb5fe; pgv_pvid=8741940233; '
              '__qc_wId=99; player=1; xsid=%s' % xsid,
    'Host': 'www.cqooc.com',
    'Referer': 'https://www.cqooc.com/login?ref=https%3A%2F%2Fwww.cqooc.com%2F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' 
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}
response = session.get(url=sign_url, headers=headers).json()
sign_id = response['id']
course_id_url = 'https://www.cqooc.com/json/mcs'
param = {
    'sortby': 'id',
    'reverse': 'true',
    'del': '2',
    'courseType': '2',
    'ownerId': sign_id,
    'limit': '10'
}
response_courseId = requests.get(url=course_id_url, params=param, headers=headers).json()
course_id = response_courseId['data'][1]['course']['id']
headers['Referer'] = 'https://www.cqooc.com/learn/mooc/structure?id=334571063'
lessons_url = 'https://www.cqooc.com/json/mooc/lessons'
params = {
    'limit': '100',
    'start': '1',
    'sortby': 'selfId',
    'reverse': 'false',
    'courseId': course_id
}
lessons_response = session.get(url=lessons_url, params=params, headers=headers).json()
data = lessons_response['data']
titles = []
resIds = []
for i in range(len(data)):
    titles.append(data[i]['title'])
    resIds.append(data[i]['resId'])
resIds.pop(0)
titles.pop(0)

for j in range(len(resIds)):
    url = 'https://www.cqooc.com/json/my/res'
    params = {
        'id': resIds[j]
    }
    join_response = session.get(url=url, params=params, headers=headers).json()
    join_url = join_response['mp4File']
    join_url = join_url.split(',')
    mp4_url = 'https://video.cqooc.com/video_new/' + join_url[1]
    mp4_response = session.get(url=mp4_url, headers=headers).content
    with open(name + '/' + titles[j] + '.mp4', mode='wb')as f:
        f.write(mp4_response)
    print(titles[j] + '下载成功')

print('下载成功')
