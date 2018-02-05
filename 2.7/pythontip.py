import this
s=this.s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)     
print s
print 'python Ö®ìø'  
print "".join([d.get(c, c) for c in s])


#2
a=2
b=3 
c="012345"
print a,b,c
print a,b,a-b,c[a:b]
print c[0:1]

a=b=c={1,2,3}
print a,b-c  
x={1,2,3,4}
y={2,4,6}
print x-y,x,y,y-x


#3
import urllib2
response = urllib2.urlopen("http://www.baidu.com")
print response.read()