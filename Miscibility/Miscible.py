import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.gridspec import GridSpec
import gc

#USER INPUTS_________________________________________________________________

time=740
ncores=150
path=r"C:\Users\nakaj\OneDrive\Desktop\2025Work\MeltScalingCollisions\FinalCollisions\0.3\90Deg\\"
outputpath=path
axesdim=22
r0=1e6
axesscale=1e6

#____________________________________________________________________________

N=500

a_samples = np.random.normal(loc=60.39, scale=15.7, size=N)
b_samples = np.random.normal(loc=7.23, scale=0.65, size=N)

xtarcore=[]
ytarcore=[]
ztarcore=[]
masslist=[]

for i in range(ncores):
    with open(f"{path}results.{time:05d}_{ncores:05d}_{i:05d}.dat","r") as file:
        mantcounter=0
        file.readline()
        file.readline()
        for line in file:

            elements=line.split()
            ID=elements[0]
            tag=int(elements[1])
            mass=float(elements[2])
            xx=float(elements[3])/r0
            yy=float(elements[4])/r0
            zz=float(elements[5])/r0
            temperature=float(elements[14])
            pressure=float(elements[11])/1e9

            if tag == 1:

                xtarcore.append(xx)
                ytarcore.append(yy)
                masslist.append(mass)

xtarcore=np.array(xtarcore)
ytarcore=np.array(ytarcore)
masslist=np.array(masslist)

xcm=(np.sum(xtarcore*masslist))/np.sum(masslist)
ycm=(np.sum(ytarcore*masslist))/np.sum(masslist)

total=0
miscible=0
envelope=0
Miscx=[]
Miscy=[]
xlist=[]
ylist=[]

for i in range(ncores):
    print(i)
    with open(f"{path}results.{time:05d}_{ncores:05d}_{i:05d}.dat","r") as file:
        mantcounter=0
        file.readline()
        file.readline()
        for line in file:

            total=total+1

            elements=line.split()
            ID=elements[0]
            tag=int(elements[1])
            mass=float(elements[2])
            xx=float(elements[3])/r0-xcm
            yy=float(elements[4])/r0-ycm
            zz=float(elements[5])/r0
            temperature=float(elements[14])
            pressure=float(elements[11])/1e9

            X=((pressure-50)/a_samples)+1
            valid=X>0

            MisTempList=7250*(X[valid])**(1/b_samples[valid])
            MisTemp=np.mean(MisTempList)
            MisTempErr=np.std(MisTempList)

            if temperature>MisTemp:

                miscible=miscible+1

                if -0.4<zz<0.4:

                    Miscx.append(xx)
                    Miscy.append(yy)

            elif -0.4<zz<0.4:

                xlist.append(xx)
                ylist.append(yy)

            if MisTemp-MisTempErr<temperature<MisTemp+MisTempErr:

                envelope=envelope+1

plt.style.use('dark_background')

fig,ax=plt.subplots(figsize=(7,6))
gs=GridSpec(1,2,width_ratios=[20,0.5],figure=fig)

scatter=ax.scatter(Miscx,Miscy,c='red',marker='.',s=1.7)
scatter=ax.scatter(xlist,ylist,c='royalblue',marker='.',s=1.7)

ax.set_xlabel(f"x ({axesscale:.0e} m)")
ax.set_ylabel(f"y ({axesscale:.0e} m)")

ticks=np.linspace(-axesdim/2,axesdim/2,5)
ax.set_xticks(ticks)
ax.set_yticks(ticks)

ax.set_xlim(-axesdim/2,axesdim/2)
ax.set_ylim(-axesdim/2,axesdim/2)

title = ax.set_title(f"Visualization of Miscible Particles")

pos = ax.get_position()
title.set_position([0.5, 1.02])
ax.set_aspect('equal')
miscper=round((miscible/total)*100,2)
miscpererr=round((envelope/(2*total))*100,2)
ax.text(0.98, 0.02, rf"Miscible %: ${miscper} \pm {miscpererr}$", transform=plt.gca().transAxes, ha='right', va='bottom', fontsize=10,c='black', 
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

plt.savefig(f"{outputpath}/Miscible.png", dpi=300)

plt.show()
#plt.close()

print(f"The fraction of miscible particles is: {miscper}+-{miscpererr}%")


           