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

Windows/Anaconda instilation(Unstable, not recommended)
[cartopy](https://scitools.org.uk/cartopy/docs/latest/installing.html)

```
conda install -c conda-forge GEOS
conda install -c conda-forge NumPy
conda install -c conda-forge Cython
conda install -c conda-forge Shapely
conda install -c conda-forge pyshp
conda install -c conda-forge six
conda install -c conda-forge PROJ
conda install -c conda-forge pillow
```
Make sure you install the above before moving on
```
conda install -c conda-forge PySimpleGUI
conda install -c conda-forge Matplotlib
conda install -c conda-forge eccodes
```
In your conda environment make sure the interpreter has all the above packages in the project