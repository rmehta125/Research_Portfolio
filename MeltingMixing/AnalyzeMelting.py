import matplotlib.pyplot as plt
import numpy as np

#USER INPUTS_________________________________________________________________

path =
outputpath = path
outputnumber = 
gamma =
angle = 
axesdim =
thickness =

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



def melting():    # Determines which particles are melted

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

        # Analyze melting

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
                
    meltfrac=round((melted/total)*100,2)

    print(f'\n    The total number of melted mantle particles is: {melted}')
    print(f'    The total number of mantle particles is: {total}')
    print(f'    The melt mass fraction is: {meltfrac}%\n')

    return xlist,ylist,xmlist,ymlist,meltfrac,timevalue



def plotting(xlist,ylist,xmlist,ymlist,meltfrac,timevalue):    # Generates a plot of the melting distribution

    print('Plotting the mantle melt...\n')

    ticks=np.linspace(-axesdim/2,axesdim/2,9)
    hour=timevalue/3600

    plt.figure(figsize=(8,6))
    plt.scatter(xlist, ylist, c='blue', s=0.5, marker='.')
    plt.scatter(xmlist,ymlist,c='red',s=0.5,marker='.')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x (1e6 m)')
    plt.ylabel('y (1e6 m)')
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.xlim(-axesdim/2,axesdim/2)
    plt.ylim(-axesdim/2,axesdim/2)
    plt.title(f'Cross Section of Melting, t={hour:0.2f} h, $\gamma={gamma}$, ${angle}^\circ$',
              multialignment='center')
    plt.text(0.98, 0.02, f'Melting %: {meltfrac}',transform=plt.gca().transAxes,ha='right', 
             va='bottom',fontsize=10,bbox=dict(facecolor='white',alpha=0.7,edgecolor='none'))
    plt.savefig(f'{outputpath}/Melting_{outputnumber:05d}.png',dpi=300)

    print(f'    Outputted Melting_{outputnumber:05d}.png\n')

    plt.show()



def main():

    xlist,ylist,xmlist,ymlist,meltfrac,timevalue=melting()
    plotting(xlist,ylist,xmlist,ymlist,meltfrac,timevalue)



main()



