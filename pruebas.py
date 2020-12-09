"""import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])

ped=[1, 2, 3, 4, 5, 6, 7]
#a = np.insert(a, 3, 0)
a[2]=1
siet=6
suped=[]
if siet==7:
    suped=ped[1:siet-1]

print(suped)

for i in range(4):
    print(i)
"""
import json
import numpy
import sys

data = numpy.array(json.loads(sys.argv[1]))
#data1 = numpy.array(json.loads(sys.argv[2]))
print(data)
#print(data1)