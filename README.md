# wrf-preprocessing
Checks and preprocessing for a WRF project.

Use the docker-compose.yml file as a template. 
Four files/folder should be mounted into the container:
1. parameters.toml - look at the parameters_example.toml
2. A namelist.wps file
2. A namelist.input file
3. The WPS_GEOG folder with all the static files to run geogrid.exe

