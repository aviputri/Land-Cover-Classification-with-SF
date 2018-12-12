import numpy as np
import rasterio
from rasterio.transform import from_origin

#2009
#load result
a = "/Volumes/ga87rif/Study Project/satelite images/result09.npy"
np_ar = np.load(a)

#reshape into 2D
b = np.reshape(np_ar, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/result09.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#2015
#load result
a = "/Volumes/ga87rif/Study Project/satelite images/result15.npy"
np_ar = np.load(a)

#reshape into 2D
b = np.reshape(np_ar, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/result15.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()

#2018
#load result
a = "/Volumes/ga87rif/Study Project/satelite images/result18.npy"
np_ar = np.load(a)

#reshape into 2D
b = np.reshape(np_ar, (-1,3057))
c = np.flipud(b) #flip vertically
#because rasterio is lame it writes from bottom to top

#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

new_dataset = rasterio.open('/Volumes/ga87rif/Study Project/Result/result18.tif', 'w', driver='GTiff',
                            height = b.shape[0], width = c.shape[1],
                            count=1, dtype=c.dtype,
                            crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
                            transform=transform)

new_dataset.write(c, 1)
new_dataset.close()