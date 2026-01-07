# Simulating the Formation of the South Pole-Aitken Basin with SPH

## Overview

This is a project I worked on to help a graduate student, Nicholas Litza, who was studying the formation of the South Pole-Aitken (SPA) basin.  The SPA basin is a massive impact crater on the far side of the Moon, estimated to be over 2500 km in diameter.  Litza was studying how this impact feature formed with the use of a simulation software known as iSALE.  However, he ran into limitations, as iSALE simulates impacts in 2 dimensions.  Additionally, in order to determine the crater diameter, the iSALE impacts would have needed to run for an unfeasible amount of time.  Therefore, I used SPH to recreate his collision scenario and produce a faster, 3D simulation.

## Methods

The impact parameters used are shown below.

<table>
<tr>
  <td>
    Collision Angle (°)
  </td>
  <td>
    Target Mass (kg)
  </td>
  <td>
    Impactor-To-Total Mass Ratio
  </td>
  <td>
    Impact Velocity (km/s)
  </td>
  <td>
    Number of Particles
  </td>
</tr>
<tr>
  <td>
    0
  </td>
  <td>
    7.35e+22
  </td>
  <td>
    0.0015
  </td>
  <td>
    10
  </td>
  <td>
    3,331,800
  </td>
</tr>
  
</table>

The impactor was assumed to have a radius of 200 km and no core.  For this project, I analyzed the pressure and energy delievered during the collision.  Additionally, I analyzed the formation of the initial crater rim and estimated its radius.  This was determined by finding all particles that were launched into orbit at an early timestep using the program DetermineTracers.py in this folder.  Then, at the final timestep of the simulation, each of these particles were tracked and their final position was plotted.

## Results and Conclusions

The animations for the energy and pressure during impact are shown below.

<div align="center">

https://github.com/user-attachments/assets/bc6738f1-5c29-432a-8277-9ecb60760ec7

</div>

The energy animation displays the energy distribution and extent of the amount of debris launched into orbit. The pressure animation shows the pressure waves after the initial impact rippling over the Moon.  Furthermore, it displays an overall destruction of the Moon during impact, as at around t = 1 h, a wave of lunar material cascades over the body.  This supported the original presumption that an impactor of this size would have resulted in the Moon's destruction.  

The crater rim and radial distribution of the crater particles are shown below.

<img width="1800" height="1800" alt="Crater" src="https://github.com/user-attachments/assets/d9413c9a-16ae-484e-b183-08512ac152aa" />

<img width="1920" height="1440" alt="CraterDist" src="https://github.com/user-attachments/assets/893537c2-69e7-4cf6-886f-07153f9ea94d" />

Overall, the initial impact crater extends to a radius of about 1,800 km.  It is worth noting, however, that in contrast to iSALE, SPH does not handle material strength and instead treats the bodies as fluids.  This may cause the location of the initial crater radius to differ slightly from iSALE results.
