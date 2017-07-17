# coding=utf8

import urllib
import urllib2


def load_page(url,file_name):
    """
    作用：根据url发送请求，获取服务器相应文件
    url: 需要爬取的url地址
    """
    print '正在下载；' + file_name
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    request = urllib2.Request(url,headers=headers)

    return urllib2.urlopen(request).read()




def write_page(html,file_name):
    """
    作用：将html内容写到本地
    :param html:
    :return:
    """
    print '正在保存'+file_name
    with open('./download/'+file_name.decode('utf8'),'w') as f:
        f.write(html)


def tieba_spider(url,bagin_page,end_page):
    '''
    作用；贴吧爬虫调度器，负责组合处理每个页面的url
    url :贴吧url前部分

    '''

    #每一页一页的爬，用for
    for i in range(bagin_page,end_page+1):
        pn = (i-1)*50 #这里是百度贴吧表示 页码的方式
        ful_url = url +'&pn=' +str(pn)
        print ful_url
        file_name = '第' + str(i) +'页.html'
        #调用load_page
        html = load_page(ful_url,file_name)
        write_page(html,file_name)


if __name__ == '__main__':
    kw = raw_input("输入贴吧名：")
    begain_page = int(raw_input('起始页:'))
    end_page = int(raw_input('输入结束页'))

    url ='https://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw':kw})

    ful_url = url  +key

    tieba_spider(ful_url,begain_page,end_page)