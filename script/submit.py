import httplib2
from re import *
h = httplib2.Http('.cache')
num = input("problem number")
address = "http://projecteuler.net/index.php?section=problems&id="+num
site = h.urlopen(address)
x = [i.decode('utf-8') for i in site]
print(x)
'''
for line in x:
    if 'Answer:' in line:print('here')

for line in site:
    l = line.decode('utf-8')
    if search('captcha',l):print('here');break
    print(l)
'''
