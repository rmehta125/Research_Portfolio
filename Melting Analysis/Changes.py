import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple

#USER INPUTS_________________________________________________________________

path =      #Path to data files
gamma =     #Impactor to total mass ratio (needed for naming the output file) 
ncores =    #Number of cores used for the simulation
time =      #Time you are analyzing the changes at

#____________________________________________________________________________

Particle = namedtuple('Particle', ['id','tag','mass','x','y','z','r','density','energy','pressure','entropy','temperature'])
particlesf=[]
particlesi=[]

print()
for i in range(ncores):
    file = f"{path}results.{time:05d}_{ncores:05d}_{i:05d}"+".dat"
    print(f"results.{time:05d}_{ncores:05d}_{i:05d}"+".dat")
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

            radius=((xx**2+yy**2+zz**2)**0.5)
            density=float(elements[9])
            energy=float(elements[10])
            pressure=float(elements[11])
            entropy = float(elements[13])
            temperature = float(elements[14])
            
            particlesf.append(Particle(ID,tag,mass,xx,yy,zz,radius,density,energy,pressure,entropy,temperature))

    file = f"{path}results.00000_{ncores:05d}_{i:05d}"+".dat"
    print(f"results.00000_{ncores:05d}_{i:05d}"+".dat")
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
            radius=((xx**2+yy**2+zz**2)**0.5)
            density=float(elements[9])
            energy=float(elements[10])
            pressure=float(elements[11])
            entropy = float(elements[13])
            temperature = float(elements[14])
            
            particlesi.append(Particle(ID,tag,mass,xx,yy,zz,radius,density,energy,pressure,entropy,temperature))

print("\n Writing Output File, Particle Number is:\n")

particlesi_dict = {p.id: p for p in particlesi}
with open(f"{path}changes{gamma}.txt", "w") as file:
    for k, particlef in enumerate(particlesf):
        particlei = particlesi_dict.get(particlef.id)
        densitychange = particlef.density - particlei.density
        energychange = particlef.energy - particlei.energy
        pressurechange = particlef.pressure - particlei.pressure
        entropychange = particlef.entropy - particlei.entropy
        temperaturechange = particlef.temperature - particlei.temperature

        file.write(f"{particlei.id} {particlei.tag} {particlef.mass} {particlef.x} {particlef.y} {particlef.z} X X X {densitychange} {energychange} {pressurechange} X {entropychange} {temperaturechange} {particlef.r}\n")
        if 0 == k % 100000:
            print(f"Particle Number: {k}")
        
print(f"\nOutputted changes{gamma}.txt\n")
