from glob import glob
import zipfile
import sys

zip_files = glob('*.zip')

if zip_files:
    for z in zip_files:
        zipfile.ZipFile(zr 'r').extractall()
else:
    print("Zip files not found")

