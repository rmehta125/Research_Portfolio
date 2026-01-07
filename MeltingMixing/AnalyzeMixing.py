import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from scipy.spatial import cKDTree
import pyvista as pv

#USER INPUTS_________________________________________________________________

path =
outputpath = 
outputnumber =
gamma = 
angle = 
axesdim = 
cameraposition = 
elevation = 
settled = 

#____________________________________________________________________________

r0=1e6

class Particle:    # Defines a particle class

    def __init__(self,tag,x,y,z,r,fate,neighbors):

        self.tag = tag
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.fate = fate
        self.neighbors = neighbors



def read_data():    # Reads and stores all data

    print('\nReading data...')

    particles=[]

    with open(f'{path}/SortedData_{outputnumber:05d}.txt','r') as file:

        timevalue=float(file.readline())
        file.readline()
        radius=float(file.readline())
        file.readline()
        cms=file.readline().split()
        xcm,ycm,zcm=float(cms[0]),float(cms[1]),float(cms[2])    

        for line in file:

            elements=line.split()
            tag=int(elements[1])
            xx=(float(elements[3])-xcm)/r0
            yy=(float(elements[4])-ycm)/r0
            zz=(float(elements[5])-zcm)/r0
            fate=int(elements[15])
            r=np.sqrt(xx**2+yy**2+zz**2)
            neighbors=0

            particles.append(Particle(tag,xx,yy,zz,r,fate,neighbors))

    return radius,particles,timevalue



def double_click_cutoff(event):    # Detects a double-click on particle distribution plot

    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.dblclick and event.inaxes == ax and event.xdata is not None:

        fig.cutoff = int(event.xdata)
        fig.vline.set_xdata([fig.cutoff])
        fig.canvas.draw_idle()

        print(f'    Cutoff = {fig.cutoff} neighbors')



def find_cutoff(radius,particles):    # Finds a cutoff for the amount of neighboring iron

    print('\nPlotting distribution of neighboring iron...\n')

    # Use a SciPy tree for fast sorting 

    ironparticles = [p for p in particles if p.tag == 3 or p.tag == 1]
    ironpositions = np.array([[p.x, p.y, p.z] for p in ironparticles])
    irontree = cKDTree(ironpositions)
    neighborradius = (radius/20)/r0  
    nearbylist=[]

    print(f'    Neighbor radius: {neighborradius*r0:0.2e} m\n')

    percent=0

    for i, particle in enumerate(ironparticles):

        xx = particle.x
        yy = particle.y
        zz = particle.z

        # Find the number of neighboring iron particles, excluding itself

        indices = irontree.query_ball_point([xx, yy, zz], r=neighborradius)
        neighbors = len(indices) - 1
        particle.neighbors=neighbors
        nearbylist.append(neighbors)

        if i % ((len(ironparticles)-1)//10) == 0:

            print(f'    {percent}% complete')

            percent=percent+10

    # Plot the distribution of neighbors and determine cutoff

    plt.figure(figsize=(7,5))
    plt.hist(nearbylist,bins=240,color='blue')
    plt.xlabel(f'Number of Iron Neighbors within {neighborradius*r0:0.2e} m')
    plt.ylabel('Count')
    plt.title('Distribution of Neighboring Iron Particles')
    plt.tight_layout()
    fig = plt.gcf()
    fig.cutoff = None
    fig.vline = plt.axvline(0,color='red',linestyle='--')
    fig.canvas.mpl_connect('button_press_event',double_click_cutoff)

    print('\n    Please double-click on a guess for the neighboring iron cutoff ' +
          '\n    in the histogram near the start of the main distribution, and ' +
          '\n    exit the plot when you are finished.\n')
    
    plt.show()

    cutoff=fig.cutoff

    return cutoff



def double_click_CMB(event):    # Detects a double-click on particle distribution plot

    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.dblclick and event.inaxes == ax and event.xdata is not None:

        fig.CMB = event.xdata
        fig.vline.set_xdata([fig.CMB])
        fig.canvas.draw_idle()

        print(f'    CMB = {fig.CMB*r0:0.2e} m')



def double_click_radial_cutoff(event):    # Detects a double-click on particle distribution plot

    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.dblclick and event.inaxes == ax and event.xdata is not None:

        fig.radialcutoff = event.xdata
        fig.vline.set_xdata([fig.radialcutoff])
        fig.canvas.draw_idle()

        print(f'    Radial cutoff = {fig.radialcutoff:0.2f} (1e6 m)')



def analyze_mixing(cutoff,particles,timevalue,radius):    # Analyzes mixing

    print('\nAnalyzing mixing...\n')

    ironparticles=[p for p in particles if p.tag == 1 or p.tag == 3]
    impcore=[p for p in ironparticles if p.tag == 3]
    core=len(impcore)
    mixed=0

    mixedx=[]
    mixedy=[]
    mixedz=[]

    sunkx=[]
    sunky=[]
    sunkz=[]

    if settled == True:

        # Determine which impactor core particles have mixed and which have sunken

        for particle in impcore:

            xx = particle.x
            yy = particle.y
            zz = particle.z
            tag=particle.tag
            fate=particle.fate
            neighbors=particle.neighbors

            if neighbors < cutoff and fate != 2 and tag == 3:

                mixed=mixed+1

                mixedx.append(xx)
                mixedy.append(yy)
                mixedz.append(zz)

            elif fate != 2 and tag == 3:

                sunkx.append(xx)
                sunky.append(yy)
                sunkz.append(zz)

    elif settled == False:

        ironr=[p.r for p in particles if p.tag == 1 or p.tag == 3]
        silir=[p.r for p in particles if p.tag == 0 or p.tag == 2]

        plt.figure(figsize=(8,6))
        plt.hist(ironr,range=(0,radius/r0),bins=240,color='blue',alpha=0.7,label='Iron')
        plt.hist(silir,range=(0,radius/r0),bins=240,color='red',alpha=0.7,label='Silicate')
        plt.ylabel('Count')
        plt.title('Radial Distribution of Particles')
        plt.legend()
        fig = plt.gcf()
        fig.CMB = None
        fig.vline = plt.axvline(0,color='green',linestyle='--')
        fig.canvas.mpl_connect('button_press_event',double_click_CMB)

        print('    Please double-click on a guess for CMB in the histogram, and '+
              '\n    exit the plot when you are finished.\n')
        
        plt.show()

        CMB=fig.CMB

        boundironr=[p.r for p in ironparticles if p.fate != 2]
        plt.figure(figsize=(8,6))
        plt.hist(ironr,range=(0,max(boundironr)),bins=500,color='blue')
        plt.xlabel('Radius (1e6 m)')
        plt.ylabel('Count')
        plt.title('Radial Distribution of Iron Particles')
        fig = plt.gcf()
        fig.radialcutoff = None
        fig.vline = plt.axvline(0,color='red',linestyle='--')
        fig.canvas.mpl_connect('button_press_event',double_click_radial_cutoff)

        print('\n    Please double-click on the radial cutoff for analysis in the '+
              '\n    histogram right before the impactor iron core, and exit the ' + 
              '\n    plot when you are finished.\n')

        plt.show()

        radialcutoff=fig.radialcutoff

        print()

        for particle in particles:

            xx = particle.x
            yy = particle.y
            zz = particle.z
            r=particle.r
            tag=particle.tag
            fate=particle.fate

            if CMB < r < radialcutoff and fate != 2 and tag == 3:

                mixed=mixed+1

                mixedx.append(xx)
                mixedy.append(yy)
                mixedz.append(zz)

            elif fate != 2 and tag == 3:

                sunkx.append(xx)
                sunky.append(yy)
                sunkz.append(zz)

    xtarcore=[p.x for p in ironparticles if p.tag == 1]
    ytarcore=[p.y for p in ironparticles if p.tag == 1]
    ztarcore=[p.z for p in ironparticles if p.tag == 1]

    print('Generating mixing plots and printing results...')

    # Generate projection plot

    ticks=np.linspace(-axesdim/2,axesdim/2,5)
    mixper=round((mixed/core)*100,2)
    hour=timevalue/3600

    plt.figure(figsize=(8,6))
    plt.scatter(mixedx,mixedy,c='red',marker='.',s=1.7)
    plt.scatter(xtarcore,ytarcore,c='gray',marker='.',s=1.7,alpha=0.08)
    plt.scatter(sunkx,sunky,c='blue',marker='.',s=1.7)       
    plt.xlabel(f'x (1e6 m)')
    plt.ylabel(f'y (1e6 m)')
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.xlim(-axesdim/2,axesdim/2)
    plt.ylim(-axesdim/2,axesdim/2)
    plt.title(fr'Projection of Mixing, t={hour:0.2f} h, $\gamma={gamma}$, ${angle}^\circ$')
    plt.text(0.98, 0.02, f'Mixing %: {mixper}',transform=plt.gca().transAxes,ha='right', 
            va='bottom',fontsize=10,bbox=dict(facecolor='white',alpha=0.7,edgecolor='none'))
    plt.gca().set_aspect('equal')
    plt.savefig(f'{outputpath}/MixingProj_{outputnumber:05d}.png',dpi=300)
    plt.show()

    # Generate 3D render

    p = pv.Plotter(off_screen=False, window_size=(2112, 1808)) 
    pv.global_theme.font.family = 'courier'
    tarcloud=pv.PolyData(np.column_stack([xtarcore,ytarcore,ztarcore]))
    sunkcloud=pv.PolyData(np.column_stack([sunkx,sunky,sunkz]))
    mixedcloud=pv.PolyData(np.column_stack([mixedx,mixedy,mixedz]))
    particlesize=8
    p.add_points(tarcloud,point_size=particlesize,color='gray',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)

    if len(sunkx) != 0 and len(mixedx) != 0:

        p.add_points(sunkcloud,point_size=particlesize,color='blue',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)
        p.add_points(mixedcloud,point_size=particlesize,color='red',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)

    p.add_title(f'3D Render of Mixing at {timevalue/3600:0.2f} h, gamma={gamma}, {angle}°',font_size=18)
    p.add_text(f'Mixing %: {mixper}     \n\n',position='lower_right',font_size=16)
    p.camera_position = [cameraposition,(0,0,0),(0,0,1)]  
    p.camera.Elevation(elevation)
    p.show()

    print(f'\n    The number of impactor core particles in the mantle is: {mixed}')
    print(f'    The total number of impactor core particles is: {core}')
    print(f'    The mixing percentage is: {mixper}%')
    print(f'\n    Outputted MixingProj_{outputnumber:05d}.png')

    anim=str(input('\nWould you like to generate the animation (Yes/No)? '))

    # Generate a 3D animation gif file, if desired

    if anim == 'Yes' or anim == 'yes':

        print('\nGenerating animation...\n')

        p = pv.Plotter(off_screen=True, window_size=(2112, 1808))
        pv.global_theme.font.family = 'courier'
        tarcloud=pv.PolyData(np.column_stack([xtarcore,ytarcore,ztarcore]))
        sunkcloud=pv.PolyData(np.column_stack([sunkx,sunky,sunkz]))
        mixedcloud=pv.PolyData(np.column_stack([mixedx,mixedy,mixedz]))
        p.add_points(tarcloud,point_size=particlesize,color='gray',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)

        if len(sunkx) != 0 and len(mixedx) != 0:

            p.add_points(sunkcloud,point_size=particlesize,color='blue',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)
            p.add_points(mixedcloud,point_size=particlesize,color='red',render_points_as_spheres=True,lighting=False,show_scalar_bar=False)

        p.add_title(f'3D Render of Mixing at {timevalue/3600:0.2f} h, gamma={gamma}, {angle}°',font_size=18)
        p.add_text(f"Mixing %: {mixper}     \n\n", position='lower_right', font_size=14)
        p.camera_position = [cameraposition,(0,0,0),(0,0,1)]  
        p.camera.Elevation(20)
        p.open_gif(f"{outputpath}/Mixing3D_{outputnumber:05d}.gif",fps=20)
        p.show(auto_close=False)  

        percent=0

        for i in range(360):

            if i % 36 == 0:

                print(f'    {percent}% complete')

                percent=percent+10

            if i == 359:

                print('    100% complete')
                print('\n    Finalizing...')

            p.camera.Azimuth(1)
            p.render()
            p.write_frame()

        p.close()

        print(f'\n    Outputted Mixing3D_{outputnumber:05d}.gif\n')

    else:

        print()



def main():

    radius,particles,timevalue=read_data()

    if settled == True:

        cutoff=find_cutoff(radius,particles)

    elif settled == False:

        cutoff=None

    analyze_mixing(cutoff,particles,timevalue,radius)




main()


