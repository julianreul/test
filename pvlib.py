# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:12:18 2017

@author: Jul
"""

import pvlib as pvl
import pandas as pd
#import numpy as np
#from scipy import constants as const
#import PV_Module as pvm
#import PV_ONE_Diode_Model_big as pvo
#%% 
array_AOI=[]
date_str = '1/1/2016'
start = pd.to_datetime(date_str) - pd.Timedelta('365 days 1 hours')
hourly_periods = 8760
drange = pd.date_range(start, periods=hourly_periods, freq='H')
#%% HH: La=53.63 Lo=10; S: La=48.68 Lo=9.22; CA: La=34.8667 Lo=-116.783
Latitude=53.63
Longitude=10
DataFrame=pvl.solarposition.spa_python(drange, Latitude, Longitude, altitude=0, pressure=101325, temperature=12, delta_t=67.0, atmos_refract=None, how='numpy', numthreads=4)
#%%
for i in range(len(DataFrame)):
    solar_zenith=DataFrame.ix[i, 'zenith']
    solar_azimuth=DataFrame.ix[i, 'azimuth']
    AOI=pvl.irradiance.aoi(30, 180, solar_zenith, solar_azimuth)
    array_AOI.append(AOI)

my_df = pd.DataFrame(array_AOI)
my_df.to_csv('my_csv_AOI.csv', index=False, header=False)