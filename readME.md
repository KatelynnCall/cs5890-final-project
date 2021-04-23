The following libraries are needed to run this program (commands given for Ubuntu install):

[python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)
```
apt-get install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt-get install -y python3.8
```

[eccodes](https://confluence.ecmwf.int/display/ECC/ecCodes+Home)
```
apt-get install -y libeccodes-tools
```

[libgeos](https://github.com/libgeos/geos) 
```
apt-get install -y libproj-dev proj-data proj-bin
apt-get install -y libgeos-dev
```

The following must be installed with pip:

```
pip3 install cdsapi
pip3 install xarray
pip3 install cfgrib
pip3 install matplotlib
pip3 install scipy
pip3 install eccodes
pip3 install eccodes-python
pip3 install PySimpleGUI
pip3 install Pillow
pip3 install cython
pip3 install cartopy
```