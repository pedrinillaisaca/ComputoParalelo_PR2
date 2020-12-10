import numpy as np
# Para importar la biblioteca random al completo
import random
import os

# Para importar sólo determinadas funciones (randrange y choice)
from random import randrange, choice
a=[]
dimension=2000
for i in range(dimension): 
    b=[]        
    for j in range(dimension):       
        b.append(random.randint(1,9))
    a.append(b)            
vec=[]
for i in range(dimension):       
        vec.append(random.randint(1,9))
data =np.asarray(a,dtype=np.int)
data1 =np.asarray(vec,dtype=np.int)
os.remove("mat.txt")
os.remove("vec.txt")
np.savetxt("mat.txt",data)
np.savetxt("vec.txt",data1)