# Import GDAL, NumPy, and matplotlib
from osgeo import gdal, gdal_array
import numpy as np

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

#import the bands
b1_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b1_r.tif', gdal.GA_ReadOnly)
b1_ar = b1_ds.GetRasterBand(1).ReadAsArray()
b1 = b1_ar.ravel()

b2_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b2_r.tif', gdal.GA_ReadOnly)
b2_ar = b2_ds.GetRasterBand(1).ReadAsArray()
b2 = b2_ar.ravel()

b3_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b3_r.tif', gdal.GA_ReadOnly)
b3_ar = b3_ds.GetRasterBand(1).ReadAsArray()
b3 = b3_ar.ravel()

b4_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b4_r.tif', gdal.GA_ReadOnly)
b4_ar = b4_ds.GetRasterBand(1).ReadAsArray()
b4 = b4_ar.ravel()

b5_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b5_r.tif', gdal.GA_ReadOnly)
b5_ar = b5_ds.GetRasterBand(1).ReadAsArray()
b5 = b5_ar.ravel()

b7_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/clip_b7_r.tif', gdal.GA_ReadOnly)
b7_ar = b7_ds.GetRasterBand(1).ReadAsArray()
b7 = b7_ar.ravel()

#import the SF 

ndvi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/ndvi.tif', gdal.GA_ReadOnly)
ndvi_ar = ndvi_ds.GetRasterBand(1).ReadAsArray()
ndvi = ndvi_ar.ravel()

ndwi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/ndwi.tif', gdal.GA_ReadOnly)
ndwi_ar = ndwi_ds.GetRasterBand(1).ReadAsArray()
ndwi = ndwi_ar.ravel()

mndwi1_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/mndwi1.tif', gdal.GA_ReadOnly)
mndwi1_ar = mndwi1_ds.GetRasterBand(1).ReadAsArray()
mndwi1 = mndwi1_ar.ravel()

mndwi2_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/mndwi2.tif', gdal.GA_ReadOnly)
mndwi2_ar = mndwi2_ds.GetRasterBand(1).ReadAsArray()
mndwi2 = mndwi2_ar.ravel()

ndbi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/ndbi.tif', gdal.GA_ReadOnly)
ndbi_ar = ndbi_ds.GetRasterBand(1).ReadAsArray()
ndbi = ndbi_ar.ravel()

mndbi_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/2015/Mosaic/mndbi.tif', gdal.GA_ReadOnly)
mndbi_ar = mndbi_ds.GetRasterBand(1).ReadAsArray()
mndbi = mndbi_ar.ravel()

#stack into a 2D array
img15_ar = np.array([b1,b2,b3,b4,b5,b7,ndvi,ndwi,mndwi1,mndwi2,ndbi,mndbi]) #2D array
img15 = img15_ar.transpose() # transposed for RF input

#save transposed array into Numpy Array file
a = "/Volumes/ga87rif/Study Project/satelite images/img15.npy"
np.save(a, img15)