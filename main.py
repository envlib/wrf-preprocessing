#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:09:38 2025

@author: mike
"""
from set_params import check_set_params
from geogrid import run_geogrid
from upload_files import upload_files

########################################
### Run sequence

check_set_params()

print('-- Run geogrid.exe')
min_lon, min_lat, max_lon, max_lat = run_geogrid()

print(min_lon, min_lat, max_lon, max_lat, sep=', ')

print('-- Upload files')
upload_files()




































