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

The first step in this project was to determine the peak temperature and pressure that occurs during the collision.  To do this, I wrote and used the MaxTempPress.py file in this folder.  This program also returns the 99.5 and 99th percentiles of temperature and pressure to guard against outliers.  The fraction of miscible particles was also determined in Miscible.py using a Monte Carlo error estimate.  Slight variations of Miscible.py were also created to generate animations of miscibility.  

## Results

Although this project is still just getting started, there are a few preliminary results that show the direction we are taking this study.  Shown below are plots for the evolution of peak temperature and pressure throughout the simulation.

<div align="center">

<img width="700" height="1189" alt="Screenshot 2026-01-07 232209" src="https://github.com/user-attachments/assets/00076ef9-9f4c-4e1f-9dcd-14bc908c6eb9" />

<img width="700" height="1169" alt="Screenshot 2026-01-07 232227" src="https://github.com/user-attachments/assets/365b1c1f-2508-4dae-b948-fc90ffced8ac" />

</div>

These plots show the extreme temperatures and pressures a collision of this size is subject, with maximum values up to 1.4e+6 K and 1.1e+4 GPa, respectively.  Animations of the temperature and pressure distributions are shown below under more moderate ranges.

<div align="center">

https://github.com/user-attachments/assets/04689133-1cce-4034-8b89-a809799a58b7

</div>

These intense conditions suggest significant miscibility, which is exactly what we see.  The following animation shows the evolution of miscibility for each material.  The target core, target mantle, impactor core, and impactor mantle are plotted in gray, green, red, and blue, respectively.  When a particle turns a lighter shade of its original color, it is considered miscible.

By the end of the animation, we can see nearly the entire body is miscible, which has significant implications for its resulting composition.  Below is a plot that summarized this animation in one figure showing evolution of miscibility for each material over time.

<img width="800" height="1800" alt="MultMatMiscEvo" src="https://github.com/user-attachments/assets/227d63db-4f33-46ba-9319-c170ae32ae36" />

Within just 6 hours, the impactor core and target cores are nearly fully miscible, with the impactor and target mantles close behind.




