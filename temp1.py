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