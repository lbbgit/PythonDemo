# coding:utf8
import urllib2,cookielib

url = "https://www.baidu.com"

print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode() #返回状态码
print len(response1.read()) #返回的网页内容的长度

print "第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode() #返回状态码
print cj    #返回cookie
print response3.read()  #返回网页内容






# coding:utf-8
import re
from bs4 import BeautifulSoup

# 示例代码片段(来自beautifulsoup官网)
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '获取所有的链接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print '获取lacie的链接'
link_node = soup.find('a',href='http://example.com/lacie')
print link_node.name,link_node['href'],link_node.get_text()

print '正则匹配'
link_node = soup.find('a', href= re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text()

print '获取p段落文字'
p_node = soup.find('p', class_="title")
print p_node.name,p_node.get_text()