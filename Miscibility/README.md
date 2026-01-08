## Overview

This is a relatively new project we have taken on, working in collaboration with Prof. Jie Deng from Princeton University.  The main goal is to understand the composition of a body following a massive impact.  In particular, we are interested in how miscibility plays a role in the material distribution and the structure of the resulting body.  Miscibility can be understood as the ability of a particle to mix and homogenize with the material surrounding it.  This property is highly dependent on the temperature and pressure of the material.  For this project, I have so far simulated a large impact and plotted the temperature and pressure distributions.  I am currently working on determining which particles are miscible.  Further detail is described below.

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

The first step in this project was to determine the peak temperature and pressure that occurs during the collision.  To do this, I wrote and used the MaxTempPress.py file in this folder.  This program also returns the 99.5 and 99th percentiles of temperature and pressure to guard against outliers.  I also plotted cross sections of the temperature and pressure distributions using the code found in the VisualizationCode folder of this repository.

## Results

Shown below are plots for the evolution of peak temperature and pressure throughout the simulation.

<div align="center">

<img width="700" height="1189" alt="Screenshot 2026-01-07 232209" src="https://github.com/user-attachments/assets/00076ef9-9f4c-4e1f-9dcd-14bc908c6eb9" />

<img width="700" height="1169" alt="Screenshot 2026-01-07 232227" src="https://github.com/user-attachments/assets/365b1c1f-2508-4dae-b948-fc90ffced8ac" />

</div>

These plots show the extreme temperatures and pressures a collision of this size is subject, with maximum values up to 1.4e+6 K and 1.1e+4 GPa, respectively.  Animations of the temperature and pressure distributions are shown below, color-coded by slightly more moderate ranges.

<div align="center">

https://github.com/user-attachments/assets/04689133-1cce-4034-8b89-a809799a58b7

</div>

These intense conditions suggest significant miscibility.  The following shows an animation of the miscibility over time for each material in the simulation.  The target core, target mantle, impactor core, and impactor mantle are plotted in gray, green, red, and blue respectively.  When a particle turns a lighter version of its original color, it is considered miscible.  The total fraction of particles that are miscible is represented by the percentage at the bottom right of the video.  Unfortunately, the methods for creating this animation and classifying particles as miscible cannot be released yet.

<div align="center">

https://github.com/user-attachments/assets/36a31b68-dcfb-428e-b8ca-868bace3a798

</div>


