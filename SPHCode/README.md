# SPH Code

## Overview

This is an ongoing project that involves testing the Nakajima Lab's SPH code, modifying it, and adding features.  The most recent version of the code can be found at the attached GitHub link which leads to the resume_test branch of the repository (https://github.com/NatsukiHosono/FDPS_SPH/tree/resume_test).  The source code can be found in the src2 folder and is based in C++.  The work that I have done so far is summarized below.

# Testing Angular Momentum

One of the tasks I completed was verifying that the SPH code conserves angular momentum.  For this, I ran a few simulations and calculated the angular mometum of each particle and plotted the net angular momentum over time.  An example is shown below for a collision involving NDunite as one of the equation of state tables.  The y-axis represents the ratio of the angular momentum at the timestep versus the angular momentum at the initial timestep.

<img width="1376" height="1029" alt="image" src="https://github.com/user-attachments/assets/636f4682-18f8-494c-a5e8-1b020ad869f5" />

<p></p>

As can be seen, angular momentum is well conserved.  Part of this investigation also involved determining the rotation period of the target bodies post-impact.  The main collision scenario I tested was the canonical impact, which is theorized to have formed the Moon.  The analysis returned a period of 5 hours after impact, which is consistent with the spin rate necessary to explain the current angular momentum of the Earth-Moon system.  The programs used for this analysis are RotationAnalysisInertia.py and MomentumAnalysis.py and are included in this folder.

# Adding a Resume Option

Another task that I took on was fixing the option to resume a collision.  Previously, framework for resuming a collision simulation from any timestep had been set up in the source code.  However, it did not function properly.  I created a new branch, resume_test, in the GitHub repository and fixed this framework in the GI.h file.  Users are now able to resume a collision from any timestep, rather than having to start it all over again.

# Fixing Particle Distributions

While working with the SPH code, I noticed that the number of particles the user inputted was not always the same as the number of particles actually added to the simulation.  Instead, the code was cutting off the total number so that it was divisible by the amount of processors being used for computation.  This posed a problem for simulations with low resolutions where this difference in particle number was more apparent.  I fixed the issue by accounting for the leftover particles and ensuring they were distributed to a processor, rather than being eliminated in the GI.h file of the source code.

# Visualization Code

In addition to fixing bugs, I also added Python programs to the repository that allowed users to visualize their collisions without the need of a complex software.  These programs along with more information about how they work can be found in the VisualizationCode folder of this repository.
