# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:19:42 2020
Code for locating points within a radius        
@author: morenodu
"""
import numpy as np
import geopy.distance
def coordinates_within_radius( coords_ref, coords_grid, radius ):
    if type(coords_grid) == np.ndarray or type(coords_grid) == list:
        new_grid = [coords_grid[i] for i in range(len(coords_grid)) if geopy.distance.distance(coords_ref, coords_grid[i]).km < radius]
    else:
        if geopy.distance.distance(coords_ref, coords_grid).km < radius:
            new_grid=coords_grid;   
    if len(new_grid) == 0:
        print('the grid is empty')    
    return new_grid
