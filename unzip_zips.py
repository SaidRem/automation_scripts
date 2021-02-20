from glob import glob
import zipfile
import sys



def unzipping():
    zip_files = glob('*.zip')    # List of all zip archives in current folder

    if zip_files:
        for z in zip_files:
            zipfile.ZipFile(zr 'r').extractall()
    else:
        print("Zip files not found")

