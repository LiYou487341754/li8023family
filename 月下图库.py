# 月下图库小程序
import os
import time
import requests
import urllib3
urllib3.disable_warnings()  # 取消警告
s = requests.session()  # 会话
s.keep_live = False

# 文件保存地址创建
filename = input("请输入保存文件夹:")
if not os.path.exists(filename):
    os.mkdir(filename)
    index = input("请输入起始索引:")
else:
    # 获取文件夹下文件数
    index = len(os.listdir(filename)) + 1

code = input("请输入口令:")
pageNum = input("请输入下载页面:")
pageSize = input("请输入一页数量:")
updateNo = input("是否下载更新图库(T/F):").upper()

# 获取数据地址参数
data_url = "https://xt.guxitk.com/api/merchant/authorByCode"
data_headers = {
    'host': 'xt.guxitk.com',
    'xweb_xhr': '1',
    'platformtype': 'weixin',
    'businessid': '1',
    'showtype': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) '
                  'NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
    'content-type': 'application/json',
    'referer': 'https://servicewechat.com/wx705151c5d15e1d1f/19/page-frame.html',
}
params = {
    'code': code,
}
# 获取参数请求
data_response = requests.get(url=data_url, params=params, headers=data_headers, verify=False).json()
data = data_response['data']['codeInfo']
merchant_id = data['merchant_id']
user_id = data['user_id']
author_id = data['author_id']

# 数据获取请求
info_url = 'https://xt.guxitk.com/api/artworks/artworksListByAuthorId'
params = {
    'merchant_id': merchant_id,
    'user_id': user_id,
    'author_id': author_id,
    'pageNum': pageNum,
    'pageSize': pageSize,
    'sort_type': '1',
    'type': ''
}

info_response = requests.get(url=info_url, params=params, headers=data_headers, verify=False).json()
img_data = info_response['data']['records']
img_headers = {
    'Sec-Ch-Ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

for i in range(len(img_data)):
    if updateNo == 'T':
        if len(str(time.localtime().tm_mon)) == 1:
            localtime = (str(time.localtime().tm_year) + '0' +
                         str(time.localtime().tm_mon) + str(time.localtime().tm_mday))
        else:
            localtime = str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday)
        if localtime == img_data[i]['cover_url'].split('/')[-1][0:8]:
            img = requests.get(url=img_data[i]['cover_url'], headers=img_headers, verify=False).content
            with open(filename + '/' + str(index) + '.jpg', 'wb')as f:
                f.write(img)
                print(img_data[i]['cover_url'].split('/')[-1] + '\t' + "下载成功")
                index = int(index) + 1
    else:
        img = requests.get(url=img_data[i]['cover_url'], headers=img_headers, verify=False).content
        with open(filename + '/' + str(index) + '.jpg', 'wb') as f:
            f.write(img)
            print(img_data[i]['cover_url'].split('/')[-1] + '\t' + "下载成功")
            index = int(index) + 1
    time.sleep(0.05)

