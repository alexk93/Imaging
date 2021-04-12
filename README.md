# About
Software for imaging applications. The Python-based software allows post processing of mass spectrometric data (XIC/EIC/TIC/SIM), partially based on the PythonMSFileReader by F. Allain. The LabVIEW-based software allows screening of a region of interest divided in steps or scans using a laser diode with shutter, Zaber stage and a mass spectrometer. 

## Main features ##
Screening:
- Offset correction in 3D
- Steps and scan screening
- user-defined application times, step widths and scan speeds
- user-defined region of interest (ROI)
- modular control of laser, shutter and stage
- online readout of absolute stage position using internal memory

Post processing:
- conversion of .raw-data into TIC/XIC/EIC, based on on the PythonMSFileReader by F. Allain
- algorithm-based, automated integration of peaks using signal thresholds, white- and blacklisting and plausability tests

## Installation Guide Python scripts ##

### Installation MSFileReader.py ##
The post processing script requires Python 3. On Windows, install Anaconda - https://www.anaconda.com/. The software was not tested on MacOS.
The python script named "MSFileReader.py" is based on the MSFIleReader by ThermoFisherScientific. For more information on installation visit https://github.com/frallain/pymsfilereader

### Installation IntegrationTool.py ###
The post processing script requires Python 3. On Windows, install Anaconda - https://www.anaconda.com/. The software was not tested on MacOS.
The post processing python script named "IntegrationTool.py" requires numpy, scipy and the statistics package.

In the windows console (start - ```cmd.exe```), make sure python is properly installed and linked to the system variables by simply typing ```python```. You should be able to see your python version. Second, go back to the console using ```Ctrl+Z```. Type
```
pip install numpy scipy
```

## How To Use The Python Scripts ##
Go to favourite console (e.g. Start - ```cmd.exe```), change dicrectory (```cd```) to the folder that includes the files and simply type
```
python MSFileReader.py path/to/file.raw
```

for raw-to-ascii conversion into ".tsv" , then hit

```
python IntegrationTool.py path/to/file.raw.tsv
```

You can use the deployed batch script "helpfulBatchfile.bat" to iterate through hundreds of .raw- and .tsv-files. To do so, please set your path in the file and run the script from a windows console, i.e. Start - ```cmd.exe```, ``` cd PATH/TO/SCRIPTANDFILES/helpfulBatchfile.bat```

Two files will be created in the directory of the script, the results and and an error file which lists "signals" excluded from the algorithm.

Please note that you need to set your parameters for integration, such as the signal threshold or the time interval between two signals ("amountspectra") and delay ("stagemovespectra") in numbers of spectra. These parameters depend on your sampling rate of the mass spectrometer and the ion current in arbitrary units. Please refer to the python script for debugging options.

## Installation Guide LabVIEW script ##

An electronic stage is needed to screen an user-defined region of interest. This VI is based on the Zaber T-LS28M ( https://www.zaber.com/products/linear-stages/T-LS/details/T-LS28M/features, WIKI: https://www.zaber.com/wiki/Manuals/T-LSM) and REQUIRES LabVIEW-driver from 

INSTALL: https://www.zaber.com/software

The shutter, mass spectrometer and laser diode are either based on TTL signalling or a simple linear scale. For obvious reasons, the shutter and laser diode require a controller and an I/O device.

It is not recommended to work with the "build application (EXE)" function of LabVIEW, as it may cause unknown issues in operability. 

## How To Use the LabVIEW VI ##
The software is mostly self-explanatory. If not, please refer to the comments inside the VI. If you still have problems, feel free to contact me at github.alexk93@gmail.com .

## IMPORTANT THOUGHTS ##
I'm always happy to see someone working with this project. I have spend lots of time coding this VI and I know that there is still plently of room for improvements, especially in clearing the algorithm. However, I'm very happy that I was able to "finish" my first big LabVIEW project. 99% of this work was done single-handedly by myself and at some points, things got crazy.

Please also note that the stage and other electronic devices are generally susceptible to electromagnetic interference from unshielded electronic devices. Yes, you may need these tin foil hats again. No, I'm not joking. I had to do it myself.

## Disclaimer ##
This software has not been excessively tested for safe use and may not be free of bugs. Please use with great care. Upon usage, you accept the MIT licence agreement.
