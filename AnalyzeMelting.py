import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

#USER INPUTS_________________________________________________________________

path=r"C:\Users\nakaj\OneDrive\Desktop\2025Work\MeltScalingCollisions\FinalCollisions\0.01\90Deg\\"
outputpath=path
outputnumber=740
gamma=0.3
angle=90
axesdim=24
thickness=0.4
cutoff=True

#____________________________________________________________________________

r0=1e6

class Particle:    # Defines a particle class

    def __init__(self,tag,x,y,z,r,press,temp):

        self.tag = tag
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.press = press
        self.temp = temp



def on_click(event):    # Detects a double-click on particle distribution plot

    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.dblclick and event.inaxes == ax and event.xdata is not None:

        fig.cutoff = event.xdata
        fig.vline.set_xdata([fig.cutoff])
        fig.canvas.draw_idle()

        print(f'    Cutoff = {(fig.cutoff*r0):0.4e} m')



def melting(cutoff):    # Determines which particles are melted

    print('\nAnalyzing melting...\n')

    xmlist=[]
    ymlist=[]
    xlist=[]
    ylist=[]
    melted=0
    total=0

    with open(f'{path}/SortedData_{outputnumber:05d}.txt','r') as file:

        timevalue=float(file.readline())
        num=float(file.readline())
        file.readline()
        file.readline()
        cms=file.readline().split()
        xcm,ycm,zcm=float(cms[0]),float(cms[1]),float(cms[2])

        i=0
        percent=0
        zmin=-thickness/2
        zmax=thickness/2

        # This if block analyzes all nonescaping particles if there is no cutoff.

        if cutoff == False:

            for line in file:

                elements=line.split()
                tag=int(elements[1])
                fate=int(elements[15])

                if tag == 0 or tag == 2:

                    if fate != 2:

                        xx=((float(elements[3]))-xcm)/r0
                        yy=((float(elements[4]))-ycm)/r0
                        zz=((float(elements[5]))-zcm)/r0
                        pressure=float(elements[11])
                        temperature = float(elements[14])

                        total=total+1

                        # Melting criteria from Rubie et al., (2015)
                        
                        if pressure*1e-9 < 24.0:

                            Tmelt=(1874.0 + 55.43 * pressure*1e-9 - 1.74 * (pressure*1e-9)**2.0  + 
                                   0.0193 * (pressure*1e-9)**3.0) 
                
                        else:    

                            Tmelt=(1249.0 + 58.28 * pressure*1e-9 - 0.395 * (pressure*1e-9)**2.0  + 
                                   0.011 * (pressure*1e-9)**3.0) 

                        if temperature > Tmelt:

                            melted=melted+1

                        if zmin < zz < zmax:

                            if temperature > Tmelt:

                                xmlist.append(xx)
                                ymlist.append(yy)
                                
                            else:

                                xlist.append(xx)
                                ylist.append(yy)

                if i % ((num-1)//10) == 0:

                    print(f'    {percent}% complete')

                    percent=percent+10

                i=i+1

        # This if block prompts the user to determine a cutoff and then analyzes all particles
        # within that distance, if cutoff is enabled.

        elif cutoff == True:
                
            particles=[]
            rlist=[]

            for line in file:

                elements=line.split()
                tag=int(elements[1])
                xx=((float(elements[3]))-xcm)/r0
                yy=((float(elements[4]))-ycm)/r0
                zz=((float(elements[5]))-zcm)/r0
                press=float(elements[11])
                temp=float(elements[14])
                r=np.array([xx,yy,zz])

                particles.append(Particle(tag,xx,yy,zz,r,press,temp))
                rlist.append(np.linalg.norm(r))

            plt.figure(figsize=(8,5))
            plt.hist(x=rlist,bins=500,range=(0,max(rlist)),color='blue')
            plt.xlabel('Radius (1e6 m)')
            plt.ylabel('Count')
            plt.title('Radial Particle Distribution')
            fig = plt.gcf()
            fig.cutoff = None
            fig.vline = plt.axvline(0,color='red',linestyle='--')
            fig.canvas.mpl_connect('button_press_event',on_click)

            print('    Please double-click on a value for the radial cutoff in the ' +
              '\n    histogram, and exit the plot when you are finished.\n')

            plt.show()

            cutoff=fig.cutoff

            print()
                
            for particle in particles:

                if particle.tag == 0 or particle.tag == 2:

                    if np.linalg.norm(particle.r) < cutoff:

                        xx=particle.x
                        yy=particle.y
                        zz=particle.z
                        pressure=particle.press
                        temperature = particle.temp

                        total=total+1

                        # Melting criteria from Rubie et al., (2015)

                        if pressure*1e-9 < 24.0: 

                            Tmelt=(1874.0 + 55.43 * pressure*1e-9 - 1.74 * (pressure*1e-9)**2.0 + 
                                   0.0193 * (pressure*1e-9)**3.0) 
                
                        else:    

                            Tmelt=(1249.0 + 58.28 * pressure*1e-9 - 0.395 * (pressure*1e-9)**2.0 + 
                                   0.011 * (pressure*1e-9)**3.0) 

                        if temperature > Tmelt:

                            melted=melted+1

                        if zmin < zz < zmax:

                            if temperature > Tmelt:

                                xmlist.append(xx)
                                ymlist.append(yy)
                                
                            else:

                                xlist.append(xx)
                                ylist.append(yy)

                if i % ((num-1)//10) == 0:

                    print(f'    {percent}% complete')

                    percent=percent+10

                i=i+1
                
    meltfrac=round((melted/total)*100,2)

    print(f'\n    The total number of melted mantle particles is: {melted}')
    print(f'    The total number of mantle particles is: {total}')
    print(f'    The melt mass fraction is: {meltfrac}%\n')

    return xlist,ylist,xmlist,ymlist,meltfrac,timevalue



def plotting(xlist,ylist,xmlist,ymlist,meltfrac,timevalue):    # Generates a plot of the melting distribution

    print("Plotting the mantle melt...\n")

    plt.figure(figsize=(8,6))
    plt.scatter(xlist, ylist, c='blue', s=1.7, marker='.')
    plt.scatter(xmlist,ymlist,c='red',s=1.7,marker='.')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x (1e6 m)')
    plt.ylabel('y (1e6 m)')
    ticks=np.linspace(-axesdim/2,axesdim/2,9)
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.xlim(-axesdim/2,axesdim/2)
    plt.ylim(-axesdim/2,axesdim/2)
    hour=round((((timevalue)//10)*10)/3600,2)
    plt.title(f'Cross Section of Melting, t={hour} h, $\gamma={gamma}$, ${angle}^\circ$',
              multialignment='center')
    plt.text(0.98, 0.02, f'Melting %: {meltfrac}',transform=plt.gca().transAxes,ha='right', 
             va='bottom',fontsize=10,bbox=dict(facecolor='white',alpha=0.7,edgecolor='none'))
    plt.savefig(f'{outputpath}/Melting_{outputnumber:05d}.png',dpi=300)

    print(f'    Outputted Melting_{outputnumber:05d}.png\n')

    plt.show()



def main(cutoff):

    xlist,ylist,xmlist,ymlist,meltfrac,timevalue=melting(cutoff)
    plotting(xlist,ylist,xmlist,ymlist,meltfrac,timevalue)



main(cutoff)
