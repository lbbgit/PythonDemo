import urllib
#import urllib2
import urllib.request

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
#try:
    # urllib.request 不能直接called，参数多
    # request = urllib.request(url)
    # response = urllib.request.urlopen(request)
    # print(    response.read())
# except urllib2.URLError, e
#     if hasattr(e, "code")
#         print        (e.code)
#     if hasattr(e, "reason")
#         print(        e.reason)


import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)