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
"""
def contar(aux):
    global lista1 
    for i in aux:
        if i[0]=="Audi":            
            lista1[0]+=float(i[1].replace("$","")) 
        elif i[0]=="Jeep":
            lista1[1]+=float(i[1].replace("$",""))
        elif i[0]=="Nissan":
            lista1[2]+=float(i[1].replace("$",""))
        elif i[0]=="Dodge":
            lista1[3]+=float(i[1].replace("$",""))           
"""
def multiplicarPosiciones(fila,rank):    
    for i in range(len(vec)):
        uno=vec[rank]
        dos=fila[i] 
        lista1[i]= uno*dos 

multiplicarPosiciones(mat[:,rank],rank)        
"""
if rank==0:
    multiplicarPosiciones(mat[:,rank],rank)
elif rank==1:
    multiplicarPosiciones(mat[:,rank],rank)
elif rank==2:
    multiplicarPosiciones(mat[:,rank],rank)
elif rank==3:
    multiplicarPosiciones(mat[:,rank],rank)
elif rank==4:
    multiplicarPosiciones(mat[:,rank],rank)
"""

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
