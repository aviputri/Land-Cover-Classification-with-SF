# Import GDAL, NumPy, and matplotlib
from osgeo import gdal, gdal_array
import numpy as np

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

#import the bands
b2_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b2_r.tif', gdal.GA_ReadOnly)
b2_ar = b2_ds.GetRasterBand(1).ReadAsArray()
b2_ar = b2_ar[0:3010,:]
b2 = b2_ar.ravel()

b3_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b3_r.tif', gdal.GA_ReadOnly)
b3_ar = b3_ds.GetRasterBand(1).ReadAsArray()
b3_ar = b3_ar[0:3010,:]
b3 = b3_ar.ravel()

b4_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b4_r.tif', gdal.GA_ReadOnly)
b4_ar = b4_ds.GetRasterBand(1).ReadAsArray()
b4_ar = b4_ar[0:3010,:]
b4 = b4_ar.ravel()

b5_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b5_r.tif', gdal.GA_ReadOnly)
b5_ar = b5_ds.GetRasterBand(1).ReadAsArray()
b5_ar = b5_ar[0:3010,:]
b5 = b5_ar.ravel()

b6_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b6_r.tif', gdal.GA_ReadOnly)
b6_ar = b6_ds.GetRasterBand(1).ReadAsArray()
b6_ar = b6_ar[0:3010,:]
b6 = b6_ar.ravel()

b7_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/clip_b7_r.tif', gdal.GA_ReadOnly)
b7_ar = b7_ds.GetRasterBand(1).ReadAsArray()
b7_ar = b7_ar[0:3010,:]
b7 = b7_ar.ravel()

#import the SF 

ndvi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/ndvi.tif', gdal.GA_ReadOnly)
ndvi_ar = ndvi_ds.GetRasterBand(1).ReadAsArray()
ndvi_ar = ndvi_ar[0:3010,:]
ndvi = ndvi_ar.ravel()

ndwi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/ndwi.tif', gdal.GA_ReadOnly)
ndwi_ar = ndwi_ds.GetRasterBand(1).ReadAsArray()
ndwi_ar = ndwi_ar[0:3010,:]
ndwi = ndwi_ar.ravel()

mndwi1_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/mndwi1.tif', gdal.GA_ReadOnly)
mndwi1_ar = mndwi1_ds.GetRasterBand(1).ReadAsArray()
mndwi1_ar = mndwi1_ar[0:3010,:]
mndwi1 = mndwi1_ar.ravel()

mndwi2_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/mndwi2.tif', gdal.GA_ReadOnly)
mndwi2_ar = mndwi2_ds.GetRasterBand(1).ReadAsArray()
mndwi2_ar = mndwi2_ar[0:3010,:]
mndwi2 = mndwi2_ar.ravel()

ndbi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/ndbi.tif', gdal.GA_ReadOnly)
ndbi_ar = ndbi_ds.GetRasterBand(1).ReadAsArray()
ndbi_ar = ndbi_ar[0:3010,:]
ndbi = ndbi_ar.ravel()

mndbi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2018/Mosaic/mndbi.tif', gdal.GA_ReadOnly)
mndbi_ar = mndbi_ds.GetRasterBand(1).ReadAsArray()
mndbi_ar = mndbi_ar[0:3010,:]
mndbi = mndbi_ar.ravel()

#stack into a 2D array
img18_ar = np.array([b2,b3,b4,b5,b6,b7,ndvi,ndwi,mndwi1,mndwi2,ndbi,mndbi]) #2D array
img18 = img18_ar.transpose() # transposed for RF input

#save transposed array into Numpy Array file
a = "/Volumes/ga87rif/Study Project/satelite images/img18.npy"
np.save(a, img18)