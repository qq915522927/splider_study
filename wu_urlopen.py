# coding=utf8
import urllib2

#发送请求返回类文件 对象
response = urllib2.urlopen('http://www.baidu.com')
# urllib2 默认的 User-Agent：Python-urllib/2.7
#
# User-Agent: 是爬虫和反爬虫斗争的第一步，养成好习惯，发送请求带User-Agent
#类文件 对象，支持文件对象的操作
html = response.read()#返回字符串

#print html


'''创建带有头部的requst请求'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
request = urllib2.Request('http://www.baidu.com/',headers=headers)
response = urllib2.urlopen(request)

#返回http响应码
code = response.getcode()
#返回 返回实际数据的url 防止重定向
url = response.geturl()

#返回响应的 报头
info = response.info()
print  response.read()




