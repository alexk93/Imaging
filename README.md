# Imaging
Software for imaging applications. The Python-based software allows post processing of mass spectrometric data (XIC/EIC/TIC/SIM), partially based on the PythonMSFileReader by F. Allain. The LabVIEW-based software allows screening of a region of interest divided in steps or scans using a laser diode with shutter, Zaber stage and a mass spectrometer. An offset correction is performed in 3D



### INSTALLATION MSFileReader.PY ###
The post processing script requires Python 3. On Windows, install Anaconda - https://www.anaconda.com/. The software was not tested on MacOS.
The python script named "MSFileReader.py" is based on the MSFIleReader by ThermoFisherScientific. For more information on installation visit https://github.com/frallain/pymsfilereader

### INSTALLATION INTEGRATIONTOOL.PY ###
The post processing script requires Python 3. On Windows, install Anaconda - https://www.anaconda.com/. The software was not tested on MacOS.
The post processing python script named "IntegrationTool.py" requires numpy, scipy and the statistics package.

In the windows console (start - cmd.exe), make sure python is properly installed and linked to the system variables by simply typing "python". You should be able to see your python version. Second, go back to the console using Ctrl+Z. Type

pip install numpy scipy

## DISCLAIMER ##
This software has not been excessively tested for safe use. Please use with great care. Upon usage, you accept the MIT licence agreement.



## INSTALLATION IMAGE.VI ###
An electronic stage is needed to screen an user-defined region of interest. This VI is based on the Zaber T-LS28M ( https://www.zaber.com/products/linear-stages/T-LS/details/T-LS28M/features, WIKI: https://www.zaber.com/wiki/Manuals/T-LSM) and REQUIRES LabVIEW-driver from 

INSTALL: https://www.zaber.com/software

The shutter, mass spectrometer and laser diode are either based on TTL signalling or a simple linear scale. For obvious reasons, the shutter and laser diode require a controller.

It is not recommended to work with the "build application (EXE)" function of LabVIEW, as it may cause unknown issues in operability. 

## HOW TO USE ##
The software is mostly self-explanatory. If not, please refer to the comments inside the VI. If you still have problems, feel free to contact me at alex.k1993@ymail.com .

## IMPORTANT THOUGHTS ##
I'm always happy to see someone working with this project. I have spend lots of time coding this VI and I know that there is still plently of room for improvements, especially in clearing the algorithm. However, I'm very happy that I was able to "finish" my first big LabVIEW project. 99% of this work was done single-handedly by myself and at some points, things got crazy.

Please also note that the stage and other electronic devices are generally susceptible to electromagnetic interference from unshielded electronic devices. Yes, you may need these tin foil hats again. No, I'm not joking. I had to do it myself.

## DISCLAIMER ##
This software has not been excessively tested for safe use. Please use with great care. Upon usage, you accept the MIT licence agreement.
