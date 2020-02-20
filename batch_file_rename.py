# Name: batch_file_rename.py
# Description: Rename fileGDB rasters

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = r"" #Edit your path

# Iterate through the files and rename them
tifFileList = arcpy.ListRasters()
for tifFile in tifFileList:
    out_data = tifFile[:] #Rename your files here
    print "Renaming {} to {}".format(tifFile, out_data)
    arcpy.Rename_management(tifFile, out_data)
