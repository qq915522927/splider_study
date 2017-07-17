# coding=utf8
import urllib2
import  urllib
import json
url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
dataform = {'tags':'电影',
            'sort':'T',
            'range':'0,10',
            'start':'0',}

data = urllib.urlencode(dataform)

request = urllib2.Request(url,data=data,headers=headers)

reponse = urllib2.urlopen(request)
a = '士大夫似的'.decode('utf8').encode('gbk')
print a
data = json.loads(reponse.read())
for x,y in  data['data'][0].items():
    print x,y

b = u'发士大夫'
print type(a),type(b)