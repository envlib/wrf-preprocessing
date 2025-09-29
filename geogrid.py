#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:16:12 2025

@author: mike
"""
import subprocess
import os
import h5netcdf
import params
import numpy as np


####################################################
### Geogrid

# os.chdir(params.wps_path)

# os.symlink(params.geogrid_exe, params.data_path.joinpath('geogrid.exe'))
# os.symlink(params.wps_path.joinpath('geogrid'), params.data_path.joinpath('geogrid'))

# p = subprocess.run(['./geogrid.exe'], cwd=params.wps_path, check=True)
# p = subprocess.run([str(params.geogrid_exe)], cwd=params.wps_nml_path.parent, check=True)

# p = subprocess.Popen([str(params.geogrid_exe)], cwd=params.data_path)

def run_geogrid():
    # f = os.open('/home/mike/data/wrf/tests/geogrid.log', os.O_WRONLY)

    p = subprocess.Popen(
            [str(params.geogrid_exe)],
            cwd=params.wps_nml_path.parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    # response = p.poll()

    stdout, stderr = p.communicate()

    print(stdout)

    with h5netcdf.File(params.data_path.joinpath('geo_em.d01.nc')) as f:
        corner_lats = f.attrs['corner_lats']
        corner_lons = f.attrs['corner_lons']

    corner_lons = [lon if lon > 0 else 360 + lon for lon in corner_lons]

    min_lon = np.floor(np.min(corner_lons))
    max_lon = np.ceil(np.max(corner_lons))
    min_lat = np.floor(np.min(corner_lats))
    max_lat = np.ceil(np.max(corner_lats))

    return min_lon, min_lat, max_lon, max_lat























































