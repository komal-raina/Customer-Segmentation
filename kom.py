from unittest import result
import numpy as np
import time
import sys

#S=range(1000)
#print(sys.getsizeof(5)*len(S))
#a=np.arange(1000)
#print(a.size*a.itemsize)

SIZE=1000000

L1=range(SIZE)
L2=range(SIZE)

A1=np.arange(SIZE)
A2=np.arange(SIZE)

new=time.time()
#result=[(x,y) for x,y in zip(L1,L2)]
#print((time.time()-new)*1000 )

new=time.time()
#result=A1+A2
#print((time.time()-new)*1000)

a=np.array([(1,2),(3,4)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)