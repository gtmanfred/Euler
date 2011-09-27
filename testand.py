from time import time
x = 10**6
t = time()
for i in range(1,x):
    a = i&1
print(time()-t)
t = time()
for i in range(1,x):
    a = i%2
print(time()-t)
