# coding=utf8
import urllib
import urllib2

def translate(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"



    #构建 有道翻译的 post请求数据

    formdata = {
    "type" : "AUTO",
    "i" : key,
    "doctype" : "json",
    "xmlVersion" : "1.8",
    "keyfrom" : "fanyi.web",
    "ue" : "UTF-8",
    "action" : "FY_BY_CLICKBUTTON",
    "typoResult" : "true"
    }
    data = urllib.urlencode(formdata)#发送的数据必须url编码


    #构造完整的头
    headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        }


    request = urllib2.Request(url,data=data,headers=headers)

    reponse = urllib2.urlopen(request)

    print(reponse.read())

if __name__ == '__main__':
    while True:
        key = raw_input("输入要翻译的英文：")
        translate(key)