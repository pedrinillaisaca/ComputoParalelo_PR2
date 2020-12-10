import numpy as np
from mpi4py import MPI 
import json
import sys
import time
comm = MPI.COMM_WORLD 
rank = comm.rank

start_time = time.time() 

mat = np.array(json.loads(sys.argv[1]))

vec=np.array(json.loads(sys.argv[2]))

lista=np.zeros(len(vec)+1,dtype=np.float)#para recibir los datos de los otros procesos
recvdata=lista

lista1=np.zeros(len(vec)+1,dtype=np.float)#formato de salida    

def multiplicarPosiciones(fila,p):    
    for i in range(len(vec)):        
        uno=vec[p]
        dos=fila[i] 
        lista1[i]+=uno*dos 
     
if rank==0:
    for i in range(0,10):
        multiplicarPosiciones(mat[:,i],i)
elif rank==1:
    for i in range(10,20):
        multiplicarPosiciones(mat[:,i],i)
elif rank==2:
    for i in range(20,30):
        multiplicarPosiciones(mat[:,i],i)
elif rank==3:
    for i in range(30,40):
        multiplicarPosiciones(mat[:,i],i)
elif rank==4:
    for i in range(40,50):
        multiplicarPosiciones(mat[:,i],i)
elif rank==5:
    for i in range(50,60):
        multiplicarPosiciones(mat[:,i],i)
elif rank==6:
    for i in range(60,70):
        multiplicarPosiciones(mat[:,i],i)
elif rank==7:
    for i in range(70,80):
        multiplicarPosiciones(mat[:,i],i)
elif rank==8:
    for i in range(80,90):
        multiplicarPosiciones(mat[:,i],i)
elif rank==9:
    for i in range(90,100):
        multiplicarPosiciones(mat[:,i],i)
end_time = time.time()
lista1[-1]=float(end_time - start_time)
#PILAS AQUI!!!!!!!!!!!!!!            
senddata = lista1
#print(" process %s sending %s " %(rank , senddata))
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
if rank==0:
    #print("Trabajando %s after Reduce: %s" % (rank,recvdata))
    print("Resultado: ", recvdata[0:-1])
    print("Tiempo: ", recvdata[len(recvdata)-1])