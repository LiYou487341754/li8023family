# 站长素材
import requests
import os
from lxml import etree


def download(url, page):
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.10171 SLBChan/11"
        }
        for i in range(page):
            if i == 0:
                detail_url = 'https://sc.chinaz.com/jianli/free.html'
            else:
                detail_url = format(url % (i+1))
            response = requests.get(url=detail_url, headers=headers).content
            tree = etree.HTML(response)
            a_list = tree.xpath('//div[@id="main"]/div/div')
            for a in a_list:
                href = a.xpath('./a/@href')
                title = a.xpath('./a/img/@alt')
                detail_data = requests.get(url=href[0], headers=headers).content
                detail_tree = etree.HTML(detail_data)
                li = detail_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')
                down = requests.get(li[0]).content
                with open(address + '/' + title[0] + '.rar', 'wb')as f:
                    f.write(down)
                    print(title[0], '下载成功')

    except Exception as e:
        print(e)


if __name__ == "__main__":
    urls = "https://sc.chinaz.com/jianli/free_%d.html"
    pn = int(input("请输入要爬取的页数:"))
    address = input("请输入要存放的文件夹:")
    if not os.path.exists(address):
        os.mkdir(address)
    download(urls, pn)
    print("下载成功")
