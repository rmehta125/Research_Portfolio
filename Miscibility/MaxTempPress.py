import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import ScalarFormatter
import numpy as np

#USER INPUTS ---------------------------------------------

path = r"C:\Users\nakaj\OneDrive\Desktop\2025Work\MassiveImpactTest\Collision\\"
outputpath = path
ncores = 200
outputnumber1 = 740
outputnumber2 = 740
r0=1e6
percentile1=99.5
percentile2=99.9

#---------------------------------------------------------

f=open(f"{outputpath}MaxTempPress.txt",'w')

for j in range(outputnumber1,outputnumber2+1):

    temperaturelist=[]
    pressurelist=[]

    for i in range(ncores):

        with open(f"{path}results.{j:05d}_{ncores:05d}_{i:05d}.dat","r") as file:

            mantcounter=0
            file.readline()
            file.readline()

            for line in file:

                elements=line.split()
                pressure=float(elements[11])/1e9
                temperature=float(elements[14])/1000
            
                pressurelist.append(pressure)
                temperaturelist.append(temperature)

    pressurelist=np.array(pressurelist)
    temperaturelist=np.array(temperaturelist)

    maxtemp=np.max(temperaturelist)
    maxpressure=np.max(pressurelist)

    per1temp=np.percentile(temperaturelist,percentile1)
    per1pressure=np.percentile(pressurelist,percentile1)

    per2temp=np.percentile(temperaturelist,percentile2)
    per2pressure=np.percentile(pressurelist,percentile2)


    fig, axes = plt.subplots(2, 1, figsize=(7, 6))

    axes[0].hist(temperaturelist, bins=500, color='plum')
    axes[0].set_ylabel("Count")
    axes[0].set_title("Temperature Distribution")
    axes[0].set_xlabel(f"Temperature (1000 K)")
    axes[0].axvline(x=per1temp,color='red',linewidth=1,linestyle='--',label=f'{percentile1}th Percentile')
    axes[0].axvline(x=per2temp,color='black',linewidth=1,linestyle='--',label=f'{percentile2}th Percentile')
    axes[0].axvline(x=maxtemp,color='blue', linewidth=1,label=f'Maximum')
    axes[0].set_xlim(0,1150)

    axes[1].hist(pressurelist, bins=500, color='plum')
    axes[1].set_xlabel(f"Pressure (GPa)")
    axes[1].set_ylabel("Count")
    axes[1].set_title("Pressure Distribution")
    axes[1].axvline(x=per1pressure,color='red',linewidth=1,linestyle='--',label=f'{percentile1}th Percentile')
    axes[1].axvline(x=per2pressure,color='black',linewidth=1,linestyle='--',label=f'{percentile2}th Percentile')
    axes[1].axvline(x=maxpressure,color='blue', linewidth=1,label=f'Maximum')
    axes[1].set_xlim(0,4600)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)
    handles, labels = axes[1].get_legend_handles_labels()

    fig.legend(handles, labels,
            loc='lower center',
            bbox_to_anchor=(0.5, 0.02),   # centered below the x-axis
            ncol=3,                        # horizontal layout
            frameon=False)
    
    f.write("{} {} {} {} {} {} {} \n".format(j, maxtemp,per1temp,per2temp,maxpressure,per1pressure,per2pressure))
    plt.savefig(f"{outputpath}Distributions_{j:05d}.png",dpi=300)

f.close()
