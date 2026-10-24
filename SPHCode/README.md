# SPH Code

## Overview

This is an ongoing project that involves testing the Nakajima Lab's SPH code, modifying it, and adding features.  The most recent version of the code can be found at the attached GitHub link which leads to the resume_test branch of the repository (https://github.com/NatsukiHosono/FDPS_SPH/tree/resume_test).  The source code can be found in the src2 folder and is based in C++.  The work I have done so far is summarized below.

## Adding a Resume Option

One task I took on was fixing the option to resume a collision.  Previously, framework for resuming a collision simulation from any timestep had been set up in the source code.  However, it did not function properly.  I created a new branch, resume_test, in the GitHub repository and fixed this framework in the GI.h file.  Users are now able to resume a collision from any timestep, rather than having to start it all over again.

## Fixing Particle Distributions

While working with the SPH code, I noticed that the number of particles the user inputted was not always the same as the number of particles truly added to the simulation.  Instead, the code was cutting off the total number so that it was divisible by the amount of processors being used for computation.  This posed a problem for simulations with low resolutions where this difference in particle number was quite apparent.  I fixed the issue by accounting for the leftover particles and ensuring they were distributed to a processor, rather than being eliminated.  This work was done the GI.h file of the source code.
