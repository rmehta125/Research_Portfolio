## Overview

This is a project I worked on to help a graduate student, Nicholas Litza, study the formation of the South Pole-Aitken basin on the Moon (SPA).  The SPA basin is a massive impact crater on the far side of the Moon, estimated to be over 2500 km in diameter.  Litza was studying how this impact feature formed with the use of a simulation software known as iSALE.  However, he ran into limitations, as iSALE simulates in 2 dimensions.  Additionally, in order to determine the crater diameter, the iSALE simulations would have needed to be run for an unfeasible amount of time.  Hence, I helped by generating a 3D simulation using SPH.

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
    3331800
  </td>
</tr>
  
</table>

The impactor was assumed to have a radius of 200 km and no core.  For this project, I analyzed the pressure and energy delievered during the collision and visualized the effect of the impact on the lunar body.  Additionally, I analyzed the formation of the crater rim.  In contrast to iSALE, SPH does not simulate material strength.  Therefore, determining the crater diameter was more of a rough estimate and proof of concept.  The crater rim was determined by finding all particles that were launched into orbit during impact using the program DetermineTracers.py.  Then, at the final timestep of the simulation, each of these particles were tracked and their final position was plotted.
