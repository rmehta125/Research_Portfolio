# Impact-Induced Melting and Mixing for Planetary Collisions

## Overview

This is by far the largest project I have taken on at the Nakajima Lab, encompassing 400+ hours of work alone.  This work is aimed at estimating the amount of melting that occurs in the target body's mantle during a collision, as well as how much of the impactor's iron core mixes with the target body's mantle.  The latter is especially important, as the iron particles that remain in the mantle can have effects on the core and mantle compositions, and subsequently the dynamo history and volatile cycle.  Previously, Nakajima developed heat scaling laws that described the amount of melting and its spatial geometry in the target mantle post-collision for collisions with impactor-to-total mass ratios (γ) above 0.03 (Nakajima et al., 2015).  My main task is to test and extend this scaling law to lower values of γ with SPH simulations.  Previous work has also been done to estimate the amount of impactor iron in the target mantle for impact velocities of 1.2 and 1.7 times the system's mutual escape velocity (e.g., Marchi et al. 2018).  Here, we extend these studies to a lower impact velocity that is equal to the system escape velocity.

So far, parts of this work have been submitted as abstracts to the Lunar and Planetary Science Conference (LPSC) and the National Conference on Undergraduate Research (NCUR) for the year 2026.  It will also soon be submitted to Rochester Symposium for Physics Students (RSPS) for 2026. We plan on writing and publishing a paper with the results.

This folder contains the programs I have written for the analysis.  SortParticles.py determines which particles are planetary, disk, and escpaing material; AnalyzeMelting.py determines the fraction of the mantle that is molten; and AnalyzeMixing.py determines the fraction of the impactor core that has mixed with the target mantle.  I have also included a file SPH_Manual_Methods.pdf, which is a document explaining the methodology behind the code as well as how to use it.

## Methods

A total of 30 SPH simulations are conducted.  Each have an impact velocity equal to the system escape velocity, as well as a target body with one Earth mass.  The impactor-to-total mass ratios tested are γ = 0.001, 0.003, 0.01, 0.03, 0.1, and 0.3.  Each body has an initial surface temperature of 2000 K.  Collisions are done at angles of θ = 0°, 30°, 45°, 60°, and 90°.  After each post-impact body reaches a steady state, we sort the particles into planetary, disk, and escaping material using an iterative scheme proposed in Canup, 2004.  We then determine which gravitationally bound silicate particles are molten based on criteria described in Rubie et al., 2015.  The amount of the impactor core that remains in the target mantle is estimated by comparing the number of neighboring iron particles for each iron particle within 0.05 times the main body radius.  For more details about how these processes work, please see SPH_Manual_Methods.pdf in this folder.

## Results

Since this is a more serious project that will eventually be published, the results will not be listed here.  They will, however, be explained at LPSC, NCUR, and RSPS, should the abstracts be accepted.  Once the results  and abstracts are formally published, a link and citation will be provided for them.

## References

Canup, R. M., 2004, Simulations of a late lunar-forming impact, Icarus, 168, 433--456, https://doi.org/10.1016/j.icarus.2003.09.028

Marchi, S., Canup, R. M., & Walker, R. J., 2018, Heterogeneous delivery of silicate and metal to the Earth by large planetesimals, Nat. Geosci., 11, 77-81, https://doi.org/10.1038/s41561-017-0022-3

Nakajima, M., Golabek, G. J., Wünnemann, K., Rubie, D. C., Burger, C., Melosh, H. J., Jacobson, S. A., Manske, L., & Hull, S. D., 2021, Scaling laws for the geometry of an impact-induced magma ocean, Earth Planet. Sci. Lett., 568, 116983, https://doi.org/10.1016/j.epsl.2021.116983
