from script.helpers import *
from time import time
t = time()
print(factors(4*10**7-1),time()-t)
t = time()
print([i for i in primetree(4*10**7-1)],time()-t)
