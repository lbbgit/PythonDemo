import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc', 'password': 'XXXX'}
headers = {'User-Agent': user_agent}
headers['Referer']='http://www.zhihu.com/articles'
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()



#proxy
enable_proxy = False  # True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
#response= urllib2.urlopen('http://www.baidu.com',timeout=10)
#response= urllib2.urlopen('http://www.baidu.com',data, 10)
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
proxy_openstr=urllib2.install_opener(opener)

print page
print proxy_openstr





# use cookie
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
