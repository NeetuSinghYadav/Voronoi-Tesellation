from scipy.spatial import Voronoi,Delaunay, ConvexHull
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import MDAnalysis
import sys


u=MDAnalysis.Universe(sys.argv[1])

sel='name CA'

atoms=u.select_atoms(sel)

#print (atoms.positions)


CA_Coords=atoms.positions

#print (CA_Coords)


vor = Voronoi(CA_Coords)

fig= plt.figure()
fig.set_size_inches(8,8)
ax=fig.add_subplot(111, projection= '3d')

for ridge_indices in vor.ridge_vertices:
	voronoi_ridge_coords = vor.vertices[ridge_indices]
	ax.plot(voronoi_ridge_coords[...,0],voronoi_ridge_coords[...,1], voronoi_ridge_coords[...,2], lw=2, c='green', alpha=0.05 )


vor_vertex_coords = vor.vertices 	

	
ax.scatter(vor_vertex_coords[...,0], vor_vertex_coords[...,1], vor_vertex_coords[...,2], c= 'orange', label = 'voronoi vertices', edgecolor='white', marker = 'o', alpha=0.8)


ax.scatter(CA_Coords[...,0], CA_Coords[...,1], CA_Coords[...,2], c= 'k', label = 'CA_coords', edgecolor='green')



ax.legend()	
ax.set_xlim3d(CA_Coords[...,0].min(), CA_Coords[...,0].max())
ax.set_ylim3d(CA_Coords[...,1].min(), CA_Coords[...,1].max())
ax.set_zlim3d(CA_Coords[...,2].min(), CA_Coords[...,2].max())




plt.show()

