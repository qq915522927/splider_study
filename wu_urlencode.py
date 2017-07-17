# coding=utf8

import  urllib

d = {'pw':'中国有嘻哈','kw':'热搜'}

#将有中文的参数，转化为url编码，接收一个字典


m = urllib.urlencode(d)
print(m)
# kw=%E7%83%AD%E6%90%9C&pw=%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%98%BB%E5%93%88

#解码成
print(type(urllib.unquote(m)))
print(type(urllib.unquote(m).decode('utf8')))

print(urllib.unquote(m).decode('utf8'))
#kw=热搜&pw=中国有嘻哈