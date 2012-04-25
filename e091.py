#!/usr/bin/env python3.2
from math import *
from time import time
t = time()
def e91(top = 50):
    count = 0
    alist = []
    points = []
    for i in range(top+1):
        for j in range(top+1):
            points.append([i,j])
    print(len(points))
    lastx = -1
    for i in points:
        if i[0]!=lastx:print(i,time()-t)
        lastx = i[0]
        for j in points:
            s1 = (i[0]**2+i[1]**2)**.5 
            s2 = (j[0]**2+j[1]**2)**.5 
            s3 = (abs(i[0]-j[0])**2+abs(i[1]-j[1])**2)**.5
            sides = [s1,s2,s3]
            if 0.0 in sides:continue
            hyp = max([s1,s2,s3])
            if hyp ==s3:
                tri = sides[0]**2+sides[1]**2-hyp**2
            elif hyp == s2:
                tri = sides[0]**2+sides[2]**2-hyp**2
            elif hyp == s1:
                tri = sides[1]**2+sides[2]**2-hyp**2
            if abs(tri)<=.00001:count+=1
    return count/2

if __name__=='__main__':
    print(e91())
