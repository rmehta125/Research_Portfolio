This is a small project I worked on to analyze the shape of a core.  Specifically, Professor Nakajima was interested in seeing how much a planetary core deforms during an impact.  The program CoreCompression.py analyzes this.  The code functions by first identifying which particles represent the surface of the core, and then drawing a triangular mesh with these particles as the vertices.  The program then fills in the mesh with planes to create a 3D surface.  Next, a line is drawn between each particle and the center of mass of the core; the lines continue until they exit the surface.  The largest line is considered to represent the maximum deformation of the core at that timestep.

An example plot created by the code is shown below for a collision with γ=0.01 at 0°. To see an interactive version, please use the following link: https://www.dropbox.com/scl/fi/r0xs5ixe65rx6u2dsljey/corecompression_00370.html?rlkey=ka9uz7vsrscfcts1qlbp8zgcb&st=6edk7wof&dl=0.

The blue particles represent target core particles, the gray shape represents the surface of the core, and the red line represents the maximum core deformation.  The code identified a length of 8.3e6 m, which corresponds to a deformation of approximately 1.8e6m from the core's original diameter.

<p></p>
<p></p>

<div align="center">

<img width="600"  alt="Screenshot 2026-01-22 142424" src="https://github.com/user-attachments/assets/3de4f4f3-1477-4df0-bb60-5b2aed92a439" />

<img width="600" alt="Screenshot 2026-01-22 142500" src="https://github.com/user-attachments/assets/626acf94-cf81-4897-a834-09e8a25b54be" />

<p></p>

</div>



