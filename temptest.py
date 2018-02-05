__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib

import urllib.request
#import urllib2
import re


class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    # def getPage_old(self, pageIndex):
    #     url = self.siteURL + "?page=" + str(pageIndex)
    #     print (url)
    #     request = urllib.request(url)# urllib2.Request(url)
    #     response = urllib.request.urlopen(request)# urllib2.urlopen(request)
    #     return response.read().decode('gbk')

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print(url)
        page = urllib.request.urlopen(url)
        html = page.read().decode('gbk')
        return html

    # 保存多张图片???
    # def saveImgs222(self, images, name):
    #     number = 1
    #     print(u"发现", name, u"共有", len(images), u"张照片")
    #     for imageURL in images:
    #         splitPath = imageURL.split('.')
    #         fTail = splitPath.pop()
    #         if len(fTail) > 3:
    #             fTail = "jpg"
    #         fileName = name + "/" + str(number) + "." + fTail
    #         self.saveImg(imageURL, fileName)
    #         number += 1
    #         # 传入图片地址，文件名，保存单张图片

    def saveImg(self, imageURL, fileName):
        imageURL="http:"+imageURL
        print(u"pic localtion:",imageURL)
        u =urllib.request.urlopen(imageURL) # urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"正在悄悄保存一张图片为", fileName)
        f.close()
        return ''

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])
            self.saveImg(item[1], "1")

spider = Spider()
spider.getContents(1)



#save 000
# info = get_content('https://tieba.baidu.com/p/2772656630')
# def get_images(info):
#     """<img src="/uploads/allimg/161026/2-1610261523390-L.jpg" alt="" width="745" height="340">"
#     """
#     regex = r'class="BDE_Image" src="(.+?\.jpg）"'
#     pat = re.compile(regex)
#
#     images_code = re.findall(pat, info)
#     print(images_code)
#     i = 0
#     for image_url in images_code:
#         print( image_url)
#         urllib.urlretrieve(image_url, '%s.jpg' % i)
#         i += 1
# print
# get_images(info)


#####2222
def saveBrief(self,content,name):
    fileName = name + "/" + name + ".txt"
    f = open(fileName,"w+")
    print (u"正在保存个人信息为",fileName)
    f.write(content.encode('utf-8'))


######33333
import os
#创建新目录
def mkdir(self,path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False


