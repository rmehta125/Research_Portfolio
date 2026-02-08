import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from scipy.spatial import cKDTree
from scipy.spatial import ConvexHull
import pyvista as pv

#USER INPUTS_________________________________________________________________

path=r"C:\Users\nakaj\OneDrive\Desktop\2025Work\MeltScalingCollisions\FinalCollisions\0.1\0Deg\\"
outputpath=path
outputnumber1=370
outputnumber2=370
ncores=200
cutoffradius=4.2e5

#____________________________________________________________________________

r0=1e6

class Particle:    # Defines a particle class

    def __init__(self,tag,m,x,y,z,r,neighbors,core):

        self.tag = tag
        self.m = m
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.neighbors = neighbors
        self.core = core



def read_data(u):    # Reads and stores all data

    print('\nReading data...\n')

    particles=[]

    percent = 0

    for i in range(ncores):

        if i % ((ncores-1)//10) == 0:

            print(f'    {percent}% complete')

            percent=percent+10

        with open(f'{path}/results.{u:05d}_{ncores:05d}_{i:05d}.dat','r') as file:

            file.readline()
            file.readline()

            # Store data

            for line in file:

                elements=line.split()
                tag=int(elements[1])
                m=float(elements[2])
                xx=(float(elements[3]))/r0
                yy=(float(elements[4]))/r0
                zz=(float(elements[5]))/r0
                r=np.sqrt(xx**2+yy**2+zz**2)
                neighbors=0

                particles.append(Particle(tag,m,xx,yy,zz,r,neighbors,False))

    x=np.array([p.x for p in particles if p.tag == 1])
    y=np.array([p.y for p in particles if p.tag == 1])
    z=np.array([p.z for p in particles if p.tag == 1])
    masslist=np.array([p.m for p in particles if p.tag == 1])

    xcm=(np.sum(x*masslist))/np.sum(masslist)
    ycm=(np.sum(y*masslist))/np.sum(masslist)
    zcm=(np.sum(z*masslist))/np.sum(masslist)  

    for p in particles:

        p.x=p.x-xcm
        p.y=p.y-ycm
        p.z=p.z-zcm

    return particles



def double_click_cutoff(event):    # Detects a double-click on particle distribution plot

    fig = event.canvas.figure
    ax = fig.axes[0]

    if event.dblclick and event.inaxes == ax and event.xdata is not None:

        fig.cutoff = int(event.xdata)
        fig.vline.set_xdata([fig.cutoff])
        fig.canvas.draw_idle()

        print(f'    Cutoff = {fig.cutoff} neighbors')



def find_cutoff(particles):    # Finds a cutoff for the amount of neighboring iron

    print('\nPlotting distribution of neighboring iron...\n')

    # Use a SciPy tree for fast sorting 

    ironparticles = [p for p in particles if p.tag == 1]
    ironpositions = np.array([[p.x, p.y, p.z] for p in ironparticles])
    irontree = cKDTree(ironpositions)
    neighborradius = cutoffradius/r0  
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



def analyze_deformation(cutoff,particles,u):    # Analyzes core deformation

    print('\nAnalyzing core deformation...\n')

    ironparticles=[p for p in particles if p.tag == 1]

    for particle in ironparticles:

        r=particle.r
        neighbors=particle.neighbors

        if neighbors > cutoff and r < 7.5:

            particle.core = True

    coreparticles = [p for p in particles if p.core == True]
    corepositions = np.array([[p.x, p.y, p.z] for p in coreparticles])
    surface = ConvexHull(corepositions,qhull_options='Qx Qt')
    vertices = corepositions
    faces = surface.simplices

    normals = []
    offsets = []

    for row in surface.equations:

        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]

        normals.append([a,b,c])
        offsets.append(d)

    surfaceindices = np.unique(surface.simplices)
    surfacepoints = corepositions[surfaceindices]

    print(f'    Number of mesh vertices: {len(surfacepoints)}\n')
    
    plotter = pv.Plotter()

    tbest=0
    maxpoint=[0,0,0]
    maxopppoint=[0,0,0]

    for i,p in enumerate(surfacepoints):  

        t=0 
        dist=np.inf
        
        for j in range(len(normals)): 

            face=surface.simplices[j]
            vertices2=corepositions[face]
            P=np.linalg.norm(p)
            h=-p/P

            distances=[]

            for point in vertices2:
            
                if np.linalg.norm(point-p) < np.linalg.norm(p):

                    break

                distances.append(np.linalg.norm(np.cross(point - p, h)) / np.linalg.norm(h))

                if len(distances) != 0:
                
                    dist1=np.mean(distances)

                else:

                    dist1=np.inf

                if dist1<dist:

                    dist=dist1

                    a=normals[j][0] 
                    b=normals[j][1] 
                    c=normals[j][2] 
                    d=offsets[j]  
                    
                    t=-(a*p[0]+b*p[1]+c*p[2]+d)/(a*h[0]+b*h[1]+c*h[2]) 

        if t > tbest:

            tbest=t
            maxpoint=p 
            maxopppoint=p+t*h

        print(f'    Vertice {i}, max deformation: {tbest:0.4f} (1e6 m)')

    faces_pv = np.hstack([np.full((faces.shape[0], 1), 3),faces]).astype(np.int64)
    mesh = pv.PolyData(vertices, faces_pv)
    plotter.add_points(np.array([[0.0,0.0,0.0]]), color="red", point_size=10)
    plotter.add_mesh(mesh,color="lightgray",opacity=0.4,smooth_shading=True)
    line = pv.Line(maxpoint, maxopppoint)
    plotter.add_mesh(line, color='red', line_width=6)
    plotter.add_points(corepositions,point_size=6,color='blue',render_points_as_spheres=True,lighting=False,show_scalar_bar=False,opacity=0.4)
    plotter.export_html(f"{outputpath}/corecompression_{u:05d}.html")
    plotter.show()



def main(outputnumber1,outputnumber2):

    for u in range(outputnumber1,outputnumber2+1):

        particles=read_data(u)
        cutoff=find_cutoff(particles)
        analyze_deformation(cutoff,particles,u)
        print()



main(outputnumber1,outputnumber2)      