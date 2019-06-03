# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import urllib

url='ftp://semdp:SEMaP+1803@hokusai.eorc.jaxa.jp/GSMaP_GNRT/DATA/2019/201905/SEMDP_GSMaP_GNRT6_0.10deg-MON_201905.nc'

filename=url[-39:]
print(filename)

urllib.request.urlretrieve(url, filename)

dataset=Dataset(filename)

print('hello abcde')


#print(dataset.dimensions.keys())