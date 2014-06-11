# OOI Instrument and Platform Exploratory Testing

The intent of this repository is to provide the code needed (mostly using
IPython Notebooks), to test, explore and examine data from OOI instruments and
platforms. This a largely an informal structure. Mostly, I'm playing and trying
out new ideas and thoughts.There are some assumptions builtin to using this
code:

1. You are an existing OOI developer comfortable working with the OOI code
framework
2. You have forked the ion-functions repo and have a local clone with all
required dependencies built out and functioning, and you are using a virtualenv
for python.
3. For lack of a better name, your virtualenv is named ion.
4. You are working on a CentOS 6.5 machine (virtual or otherwise).

If those assumptions have been met, following the next steps (after forking and
cloning this code) should get you up and running with the ability to
create/edit/explore the testing world.

## Adding dependicies
From a terminal:
```bash
sudo yum -y install geos-devel gdal-devel
```

## Adding extra python packages
```bash
workon ion
pip install --upgrade ipython[all]
pip install matplotlib
pip install basemap --allow-external basemap --allow-unverified basemap
pip install netCDF4
pip install requests
pip install bokeh
```

## Clone the OOI Toolkit, build it and install it
```bash
cd ~/dev/code
git clone git@github.com:ooici/ooitk.git
cd ooitk
python setup.py build
python setup.py install
```
## Clone (or fork and colaborate) Testing
```bash
git clone git@github.com:cwingard/testing.git
cd testing
ipython create profile
```

# That’s it.

To see some example of how to use the above to look at the
data, look in ~/dev/code/testing/platforms/cp02pmci.