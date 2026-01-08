# SPH Code

## Overview

This is an ongoing project that involves testing the Nakajima Lab's SPH code, modifying it, and adding features.  The version of the code that I worked on can be found at the attached GitHub link which leads to the drift_test branch of the repository (https://github.com/NatsukiHosono/FDPS_SPH/tree/drift_test).  The code is based primarily in C++ with a few Python programs to help it run.  The work that I have done so far is summarized below.

# Testing Angular Momentum

One of the tasks I completed was verifying that the SPH code conserves angular momentum.  For this, I ran a few simulations and calculated the angular mometum of each particle and plotted the net angular momentum over time.  An example is shown below for a collision involving NDunite as one of the equation of state tables.  The y-axis represents the ratio of the angular momentum at the timestep versus the angular momentum at the initial timestep.

<img width="1376" height="1029" alt="image" src="https://github.com/user-attachments/assets/636f4682-18f8-494c-a5e8-1b020ad869f5" />

As can be seen, angular momentum is well conserved.  Part of this investigation also involved determining the rotation period of the target bodies post-impact.
