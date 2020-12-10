import numpy as np
import json
#import sys
import time


start_time = time.time() 
def prodmv(c, B, tam):
    a = list()
    for i in range(tam):
        sum = 0
        for j in range(tam):
            sum += B[i][j] * c[j]
        a.append(sum)
    #print(a)


#mat = np.array(json.loads(sys.argv[1]))
mat = np.loadtxt('mat.txt',dtype=np.int)
#vec=np.array(json.loads(sys.argv[2]))
vec=np.loadtxt('vec.txt',dtype=np.int)

prodmv(vec, mat, len(vec))

end_time = time.time()

#print('Tiempo: {:,.2f}'.format(float(end_time - start_time)))
print("Tiempo: ",float(end_time - start_time))
