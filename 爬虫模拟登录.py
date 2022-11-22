import requests
from lxml import etree

# 获取验证码图片

jpg_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.10171 SLBChan/11"
}
session = requests.Session()
res = session.get(url=jpg_url, headers=headers, proxies={'HTTP': "119.8.25.235"})
response = res.text
print(session.cookies)
tree = etree.HTML(response)
src = tree.xpath('//*[@id="imgCode"]/@src')[0]
viewstate = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
viewstategenerator = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
data_url = 'https://so.gushiwen.cn/' + src
detail = session.get(url=data_url, headers=headers, proxies={'HTTP': "119.8.25.235"}).content
with open('./code.png', 'wb')as f:
    f.write(detail)
yzm = input('请输入验证码:')
sign_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
formdata = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': ' ',
    'email': '19823503224',
    'pwd': 'LIyou6976',
    'code': yzm,
    'denglu': '登录'
}
res1 = session.post(url=sign_url, params=formdata, headers=headers, allow_redirects=False, proxies={'HTTP': "119.8.25.235"})
print(session.cookies)
print(res1.status_code)
res1_sign = res1.headers['Location'].split(',')[0]
print(res1_sign)
sign_down = session.get(url=res1_sign, headers=headers, allow_redirects=False, proxies={'HTTP': "119.8.25.235"})
print(sign_down.status_code)
print(session.cookies)
url_sign = sign_down.headers['Location']
print(url_sign)
sign_up = session.get(url=url_sign, headers=headers, proxies={'HTTP': "119.8.25.235"}).text
print(session.cookies)
with open('./xue.html', 'w', encoding='utf-8')as f:
    f.write(sign_up)


