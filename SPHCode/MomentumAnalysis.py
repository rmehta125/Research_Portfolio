import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

#USER INPUTS ----------------------------------------------------------------

path=r"/home/theia/roshanm125/NDunite/45Degree/0.1Col/"
outputpath=r"/home/theia/roshanm125/NDunite/45Degree/0.1Col/"
ncores=100
timestep1=0
timestep2=200

#----------------------------------------------------------------------------

timesteplist=[]
Llist=[]
plist=[]

print()

f=open(f"{outputpath}/MomentumData.txt","w")

for j in range(timestep1,timestep2+1):

    pnet=np.array([0,0,0])
    Lnet=np.array([0,0,0])

    for i in range(ncores):
        
        file = f"{path}results.{j:05d}_{ncores:05d}_{i:05d}"+".dat"
        print(f"results.{j:05d}_{ncores:05d}_{i:05d}"+".dat")
        with open(file, "r") as file:
            file.readline()
            file.readline()
            for line in file:
                elements=line.split()
                ID = int(elements[0])
                tag = int(elements[1])
                mass = float(elements[2])
                xx = float(elements[3]) 
                yy = float(elements[4])
                zz = float(elements[5])
                vx = float(elements[6])
                vy = float(elements[7])
                vz = float(elements[8])
                v = np.array([vx,vy,vz])
                r = np.array([xx,yy,zz])
                p = mass*v
                L = mass*np.cross(r,v)
                pnet = pnet + p
                Lnet = Lnet + L

    f.write(f"{np.linalg.norm(Lnet)} {np.linalg.norm(pnet)}\n")





