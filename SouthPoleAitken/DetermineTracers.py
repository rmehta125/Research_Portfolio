import numpy as np

timestep=100
ncores=400
path=r"C:\Users\nakaj\OneDrive\Desktop\2025Work\SPACollision\Results\\"
outputpath=r"C:\Users\nakaj\OneDrive\Desktop\2025Work\SPACollision\\"

xcore=[]
ycore=[]
zcore=[]
masslist=[]

xlist=[]
ylist=[]
zlist=[]

for j in range(ncores):

    print(j)

    file = f"{path}results.{timestep:05d}_{ncores:05d}_{j:05d}.dat"

    with open(file, 'r') as file:

        file.readline()
        file.readline()

        for line in file:

            elements=line.split()
            id=int(elements[0])
            tag=int(elements[1])
            mass=float(elements[2])
            x=float(elements[3])/1e6
            y=float(elements[4])/1e6
            z=float(elements[5])/1e6

            if tag == 1:

                xcore.append(x)
                ycore.append(y)
                zcore.append(z)
                masslist.append(mass)

xcore=np.array(xcore)
ycore=np.array(ycore)
zcore=np.array(zcore)
masslist=np.array(masslist)

xcm=(np.sum(xcore*masslist))/(np.sum(masslist))
ycm=(np.sum(ycore*masslist))/(np.sum(masslist))
zcm=(np.sum(zcore*masslist))/(np.sum(masslist))     

f = open(f'{outputpath}tracers.txt','w',newline='')

for j in range(ncores):

    print(j)

    file = f"{path}results.{timestep:05d}_{ncores:05d}_{j:05d}.dat"

    with open(file, 'r') as file:

        file.readline()
        file.readline()

        for line in file:

            elements=line.split()
            id=int(elements[0])
            tag=int(elements[1])
            mass=float(elements[2])
            x=float(elements[3])/1e6-xcm
            y=float(elements[4])/1e6-ycm
            z=float(elements[5])/1e6-zcm

            if np.sqrt(x**2+y**2+z**2) > 2:

                f.write(f"{id}\n")

f.close()






            
