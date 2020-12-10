import numpy as np
from mpi4py import MPI 
import time
comm = MPI.COMM_WORLD 
rank = comm.rank

#mat = np.array(json.loads(sys.argv[1]))
#vec=np.array(json.loads(sys.argv[2]))

mat = np.loadtxt('mat.txt',dtype=np.int)
vec=np.loadtxt('vec.txt',dtype=np.int)
start_time = time.time() 
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
def multiplicarPosiciones(fila,puntero):         
    for i in range(len(vec)):
        uno=vec[puntero]
        dos=fila[i] 
        lista1[i]+=uno*dos 

#multiplicarPosiciones(mat[:,rank],rank)    
# 

for i in range(rank*100,(rank*100)+100):
    multiplicarPosiciones(mat[:,i],i)

"""
if rank==0:
    for i in range(0,100):
        multiplicarPosiciones(mat[:,i],i)
elif rank==1:
    for i in range(100,200):
        multiplicarPosiciones(mat[:,i],i)
elif rank==2:
    for i in range(200,300):
        multiplicarPosiciones(mat[:,i],i)
elif rank==3:
    for i in range(300,400):
        multiplicarPosiciones(mat[:,i],i)
elif rank==4:
    for i in range(400,500):
        multiplicarPosiciones(mat[:,i],i)
elif rank==5:
    for i in range(500,600):
        multiplicarPosiciones(mat[:,i],i)
elif rank==6:
    for i in range(600,700):
        multiplicarPosiciones(mat[:,i],i)
elif rank==7:
    for i in range(700,800):
        multiplicarPosiciones(mat[:,i],i)
elif rank==8:
    for i in range(800,900):
        multiplicarPosiciones(mat[:,i],i)
elif rank==9:
    for i in range(900,1000):
        multiplicarPosiciones(mat[:,i],i)
"""

end_time = time.time()
lista1[-1]=float(end_time - start_time)
#PILAS AQUI!!!!!!!!!!!!!!            
senddata = lista1
#print(" process %s sending %s " %(rank , senddata))
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
if rank==0:
    #print("Trabajando %s after Reduce: %s" % (rank,recvdata))
    #print("Resultado: ", recvdata[0:-1])
    print("Tiempo: ", recvdata[len(recvdata)-1])
