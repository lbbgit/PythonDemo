#import urllib2
import urllib
import urllib2
import urllib.request


# print(urllib.__file__)
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


html = getHtml("http://www.baidu.com")

print(html)

#response = urllib2.urlopen("http://www.baidu.com")

#response = urllib.request.urlopen("http://www.baidu.com")
#print(
#response.read()
#)
# ### Ctrl+/
google =  urllib.request.urlopen('http://www.cctv.com')
print( 'http header:/n', google.info()  )
print ('http status:', google.getcode())
print ('url:', google.geturl() )
for line in google: # 就像在操作本地文件
    print(line)
google.close()


#test2
print ('test2')
#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

print (html)



#test3
import re
import urllib
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

print('test3')
html = getHtml("http://tieba.baidu.com/p/2460150866")
result=getImg(html)
print(result)