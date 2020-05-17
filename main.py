import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Load in 3d point cloud file
file_data_path="ptsFiles/subset.pts"
point_cloud= np.loadtxt(file_data_path, skiprows=1, max_rows=100000000)
mean_Z=np.mean(point_cloud,axis=0)[2]

spatial_query=point_cloud[abs( point_cloud[:,2]-mean_Z)<1]
xyz=spatial_query[:,:3]
rgb=spatial_query[:,3:]

ax = plt.axes(projection='3d')
ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], c = rgb/255, s=0.01)

plt.show()

