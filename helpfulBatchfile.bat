@echo off
Rem simply iterates trhough a user-specified folder and runs the script on each file. Change "Path-to-file" and "Path-to-download" to your absolute path, e.g. C:\data\data.tsv.
Rem The batch file needs to be placed in the same folder that contains your .tsv-data!
for /f %%f in ('dir /b "PATH-TO-FILE\*.tsv"') do python "PATH-TO-DOWNLOAD\IntegrationTool.py" %%f