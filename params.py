#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:03:38 2025

@author: mike
"""
import tomllib
import os
import pathlib
import f90nml
import shlex
import subprocess

############################################
### Read params file

base_path = pathlib.Path(os.path.realpath(os.path.dirname(__file__)))

with open(base_path.joinpath("parameters.toml"), "rb") as f:
    file = tomllib.load(f)


##############################################
### Assign executables

# wrf_path = pathlib.Path(file['executables']['wrf_path'])

# wrf_exe = wrf_path.joinpath('main/wrf.exe')

# real_exe = wrf_path.joinpath('main/real.exe')

wps_path = pathlib.Path('/WPS')

geogrid_exe = wps_path.joinpath('geogrid.exe')

# metgrid_exe = wps_path.joinpath('metgrid.exe')


###########################################
### Others

data_path = pathlib.Path('/data')

wps_nml_path = pathlib.Path('/namelist.wps')
wrf_nml_path = pathlib.Path('/namelist.input')


##########################################
### ERA5


#######################################################
### Functions


def create_rclone_config(name, config_path, config_dict):
    """

    """
    type_ = config_dict['type']
    config_list = [f'{k}={v}' for k, v in config_dict.items() if k != 'type']
    config_str = ' '.join(config_list)
    config_path = config_path.joinpath('rclone.config')
    cmd_str = f'rclone config create {name} {type_} {config_str} --config={config_path} --non-interactive'
    # print(cmd_str)
    cmd_list = shlex.split(cmd_str)
    p = subprocess.run(cmd_list, capture_output=True, text=True, check=True)

    return config_path




















