# coding=utf8
import urllib
import urllib2
from lxml import etree
import json
from threading import Thread
from Queue import Queue

CRAWL_EXIT = False
PARSE_EXIT = False


# url = 'https://www.qiushibaike.com/text/page/1/'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
#
# request = urllib2.Request(url,headers=headers)
#
# html = urllib2.urlopen(request).read()
#
# text = etree.HTML(html)
#
# #创建 模糊查询的根节点，包含每条段子的全部信息
# node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
#
# items = {}
# for node in node_list:
#     #内容,取出标签下的内容 第一个标签 text
#     content = node.xpath('.//div[@class="content"]/span')[0].text
#
#     #用户名
#     try:
#         username = node.xpath('./div[1]/a[2]/h2')[0].text
#     except:
#         print '没有用户'
#     items ={'username':username,
#      'content':content}
#     with open("qiushi.json","a+") as f:
#         f.write(json.dumps(items,ensure_ascii=False).encode('utf8')+'\n')
class ThreadCrawl(Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        super(ThreadCrawl, self).__init__()
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.threadName = threadName
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

    def run(self):
        while not CRAWL_EXIT:
            try:
                # 默认block为true，当队列空时堵塞，直到有新的元素加入队列
                page = self.pageQueue.get()
                url = 'https://www.qiushibaike.com/text/page/%d/' % page
                request = urllib2.Request(url, headers=self.headers)
                response = urllib2.urlopen(request).read()
                self.dataQueue.put(response)
            except:
                pass


class ThreadParse(Thread):
    def __init__(self, parseName, dataQueue, fileName):
        super(ThreadParse, self).__init__()
        self.dataQueue = dataQueue
        self.parseName = parseName
        self.fileName = fileName

    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass

    def parse(self, html):
        text = etree.HTML(html)

        # 创建 模糊查询的根节点，包含每条段子的全部信息
        node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')

        items = {}
        for node in node_list:
            # 内容,取出标签下的内容 第一个标签 text
            content = node.xpath('.//div[@class="content"]/span')[0].text

            # 用户名
            try:
                username = node.xpath('./div[1]/a[2]/h2')[0].text
            except:
                print '没有用户'
            items = {'username': username,
                     'content': content}
            self.fileName.write(json.dumps(items, ensure_ascii=False).encode('utf8') + '\n')


def main():
    # 页码队列
    pageQueue = Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)

    # 表示采集好的html源码队列
    dataQueue = Queue()

    crawlList = ['采集线程一号', '采集线程二号', '采集线程三号']

    # 启动三个采集线程
    thread_carwl = []
    for tname in crawlList:
        thread = ThreadCrawl(tname, pageQueue, dataQueue)
        thread.start()
        thread_carwl.append(thread)

    praseList = ['解析线程一号', '解析线程二号', '解析线程三号']
    prase_thread = []
    fileName = open('duanzi.json', 'a')
    for tname in praseList:
        thread = ThreadParse(tname, dataQueue, fileName)
        thread.start()
        prase_thread.append(thread)

    # 页码对列不为空时
    while not pageQueue.empty():
        pass

    global CRAWL_EXIT
    CRAWL_EXIT = True

    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True

    # 主线程堵塞，等待采集线程完成
    for thread in thread_carwl:
        thread.join()
        print('采集完成')

    for thread in prase_thread:
        thread.join()
        print('写入完成')


if __name__ == '__main__':
    main()
