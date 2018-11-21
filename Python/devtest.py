from __future__ import print_function

import numpy as np
from tigre.geometry import geometry
from tigre.geometry_default import TIGREParameters
import tigre_demo_file.Test_data.data_loader as data_loader
from tigre.Ax import Ax
from tigre.Atb import Atb
from tigre.Algorithms.FDK import FDK
from tigre.Algorithms.SIRT import SIRT
from tigre.Algorithms.SART import SART
from tigre.Algorithms.OS_SART import OS_SART
from tigre.Utilities.plotproj import plotproj
from tigre.Utilities.plotproj import ppslice
from tigre.Utilities.plotImg import plotImg
from matplotlib import pyplot as plt
#---------------GEOMETRY---------------------------

geo = TIGREParameters(high_quality=False)
source_img = data_loader.load_head_phantom(number_of_voxels=geo.nVoxel)
geo.mode = 'cone'


#---------------------ANGLES--------------------------------------------

angles_1 = np.linspace(0, 2*np.pi, 100, dtype=np.float32)
angles_2 = np.ones((100),dtype=np.float32)*np.array(np.pi/4, dtype=np.float32)
angles_3 = np.zeros((100),dtype=np.float32)
angles= np.vstack((angles_1,angles_3,angles_3)).T
#--------------------PROJECTION----------------------
proj_1 = Ax(source_img,geo,angles,'interpolated')
#--------------------Back Projection ----------------
ossart = OS_SART(proj_1,geo,angles,niter=5, **dict(blocksize = 1))
sart = SART(proj_1,geo,angles,niter=5)
plt.imshow(np.hstack((ossart[32],sart[32])))
plt.show()
#fdk = FDK(proj_1,geo,angles)

#---------------PLOTS-------------------------------

#plotImg(np.hstack((sirt,fdk)))
#plotImg(ossart)