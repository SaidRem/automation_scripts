"""
The script takes all .zip files in the current working directory and
unzips in the directory.
Optionally, file(s) can be specified as argumnets.
"""

from glob import glob
import zipfile
import sys



def unzipping():
    zip_files = glob('*.zip')    # List of all zip archives in current folder

    if zip_files:
        for z in zip_files:
            zipfile.ZipFile(z, 'r').extractall()
    elif len(sys.argv) > 1:
        for z in sys.argv[1:]:
            zipfile.ZipFile(z, 'r').extractall()
    else:
        print("Zip files not found")

