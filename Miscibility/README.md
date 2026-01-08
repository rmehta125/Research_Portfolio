## Overview

This is a relatively new project I have taken on, now that my analysis of impact-induced melting and mixing begins to draw to a close (see the MeltingMixing folder of this repository).  This project is in collaboration with Prof. Jie Deng from Princeton University.  The main goal is to understand the composition of a body following a massive impact.  In particular, we are interested in how miscibility plays a role in the material distribution and the structure of the resulting body.  Miscibility can be understood as the ability of a particle to mix and homogenize with the ambient material surrounding it.  This property is highly dependent on the temperature and pressure of the material.  For this project, I have so far simulated a large impact and plotted the temperature and pressure distributions, and used them to determine which particles are miscible.  Further detail is described below.

## Methods

The collision parameters used are listed below.

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
    Impact Velocity (system escape velocity)
  </td>
  <td>
    Number of Particles
  </td>
</tr>
<tr>
  <td>
    45
  </td>
  <td>
    5.9722e+25
  </td>
  <td>
    0.33
  </td>
  <td>
    1
  </td>
  <td>
    1,500,000
  </td>
</tr>
</table>

The first step in this project was to determine the peak temperature and pressure that occurs during the collision.  To do this, I wrote and used the MaxTempPress.py file in this folder.  This program also returns the 99.5 and 99th percentiles of temperature and pressure to guard against outliers.  The fraction of miscible particles was also determined in Miscible.py based on if their temperatures were higher than 

![equation](https://latex.codecogs.com/svg.image?\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt{\pi}}{2})
