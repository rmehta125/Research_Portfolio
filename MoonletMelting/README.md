# Analysis of Mantle Melting for a Collision Between Two Half-Moon Sized Bodies

## Overview

This is a small project I worked on to help a postdoctoral researcher, Thea Fardini, with her current research.  Fardini is studying the amount of tidal heating that occurs in a system with multiple moonlets before they collide.  As such, she needed a rough baseline of the amount of heating and melting that occurs during a collision.  This is especially relevant to our Earth-Moon system, as zircons have been discovered on the Moon that are around 100 Myr younger than the Moon itself, indicating that the material was molten 100 Myr after formation.  My task was to create an example collision between two bodies, each with half the mass of the Moon, and analyze the amount of melting that occurs in the mantle.

## Methods

The parameters for the collision are shown below.

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
    Impact Velocity 
    (system escape velocity)
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
    3.68e+22
  </td>
  <td>
    0.5
  </td>
  <td>
    1
  </td>
  <td>
    1,500,000
  </td>
</tr>
  
</table>

The amount of mantle melt was analyzed using a slight modification of the AnalyzeMelting.py file in the MeltingMixing folder of this repository.  Instead of tracking only the gravitationally bound silicate particles, the melting code used for this project tracked all silicate particles.  This was mainly because the process of separating particles into planetary, disk, and escaping material can take very long for just one timestep, and Fardini was interested in the evolution of melting over all timesteps.  Therefore, we decided to simplify the calcuation.  More information about how the melting code works can be found in the SPH_Manual_Methods.pdf file in the MeltingMixing folder.  

## Results and Conclusions

The results of the melting analysis were compiled into an animation and a plot showing how the mantle melt-mass fraction evolves over each timestep, where each timestep = 100s.  Both are shown below; the melting percentage shown in each represents the fraction of molten silicate particles to total silicate particles.

<div align="center">

https://github.com/user-attachments/assets/c4460e4b-5902-4d04-85e9-5b81b34e4e63

<img width="800" alt="MeltingEvoPlot" src="https://github.com/user-attachments/assets/c595f0dd-285b-4f35-8fd7-2ec249bc2758" />

</div>

<p></p>

The percentage of mantle melting stabilizes at 82%.  As shown in the animation, the entire main body appears molten, with additional molten and solid material orbitting it in a debris disk.  Overall, this serves as a proof of concept that the most energetic impacts can melt the entirety of a moonlet.



