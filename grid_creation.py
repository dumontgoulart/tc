import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import seaborn as sns
import geopy.distance

DS_1=xr.open_dataset("IBTrACS.NA.v04r00.nc")
DS_prec=xr.open_mfdataset(["era5_prec_1980_90.nc","era5_prec_1991_99.nc","era5_prec_2000_2017.nc"],combine='by_coords')
DS_1=DS_1.isel(storm=slice(1611,1615,1))
#%% Create vectors for other purposes
'''

# season = []
# name = []
# lat=[]
# lon=[]
# pres=[]
# wind=[]
# cat=[]

# for i in range(len(DS_1.storm)):
#     if DS_1['season'][i].values >= 1980 :
#         season.append(DS_1['season'][i].values)
#         name.append(DS_1['name'][i].values)
#         lat.append(DS_1['lat'][i].values)
#         lon.append(DS_1['lon'][i].values)
#         pres.append(DS_1['usa_pres'][i].values)
#         wind.append(DS_1['usa_wind'][i].values)
#         cat.append(DS_1['usa_sshs'][i].values)


#%% Define grid for test
# radius=500
# coords_ref = (30, -70)
# scale_lat=6
# lon = np.arange(coords_ref[1] - scale_lat,coords_ref[1] + scale_lat, 0.25)
# lat = np.arange(coords_ref[0] - scale_lat,coords_ref[0] + scale_lat,0.25)
# df_array=np.zeros((len(lon)*len(lat), 2))

# count=0
# for i in range(len(lon)):
#     for j in range(len(lat)):
#         coords_grid[count] =[lat[j],lon[i]]
#         count=count+1

'''
#%% Code for locating points within a radius        
def coordinates_within_radius( coords_ref, coords_grid, radius ):
    if type(coords_grid) == np.ndarray or type(coords_grid) == list:
        new_grid = [coords_grid[i] for i in range(len(coords_grid)) if geopy.distance.distance(coords_ref, coords_grid[i]).km < radius]
    else:
        if geopy.distance.distance(coords_ref, coords_grid).km < radius:
            new_grid=coords_grid;   
    if len(new_grid) == 0:
        print('the grid is empty')    
    return new_grid

#%% define multi-dimensional array

radius=500
scale_lat=6
master_grid = np.zeros((len(DS_1.storm), len(DS_1.date_time)), dtype=object)
for i in range(len(DS_1.storm)):
    for j in range(len(DS_1.date_time)):
        if np.isnan(DS_1['lat'][i,j].values) == False:
            coords_ref = [DS_1['lat'][i,j].values, DS_1['lon'][i,j].values]
            lon = np.arange(coords_ref[1] - scale_lat,coords_ref[1] + scale_lat, 0.25)
            lat = np.arange(coords_ref[0] - scale_lat,coords_ref[0] + scale_lat, 0.25)
            coords_grid=np.zeros((len(lon) * len(lat), 2))
            coords_grid = [[lat[y],lon[x]] for x in range(len(lat)) for y in range(len(lon))]
            new_grid=coordinates_within_radius(coords_ref, coords_grid, radius)
        else:
            new_grid = float('NaN')
        
        master_grid[j,i]=new_grid
        # master_grid=np.reshape(master_grid,())
