#python 2.7.14  --  urllib2
import urllib2

url = "http://www.baidu.com"
#      urllib.request.urlopen(url).
data = urllib2.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

#                  urlopen(url, data, timeout)
response = urllib2.urlopen("http://www.baidu.com")
data2=response.read().decode('UTF-8')

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
data3=response.read().decode('UTF-8')

#                  false  false
print ('result:',data==data2,data==data3)

print  len(data),len(data2),len(data3)



#urllib ,urllib2
import urllib
import urllib2
#等效于如下
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
#等效于如上
values = {"username": "1016903103@qq.com", "password": "XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()


#以上是Post，这里是Get
values = {"username": "1016903103@qq.com", "password": "XXXX"}
data = urllib.urlencode(values)
geturl = "http://passport.csdn.net/account/login" + "?"+data

