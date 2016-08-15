#coding:utf-8
import requests
import cookielib
import urllib2
cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
    
response = requests.get('http://www.baidu.com')
cookies = response.cookies
print '/n'

for item in cookies:
    print 'Name = '+item.name
    print 'Value = '+item.value