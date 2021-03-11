import sys
import os

files_list = []

for cur_dir, sub_dirs, cur_files in os.walk(file_path):
    for f in cur_files:
        full_path = os.path.join(cour_dir, f)
        size_f = os.path.getsize(full_path)
        files_list.append((full_path, size_f))



# TODO
# The func can recieve a file path from sys.argv or clipboard
# The func can recieve file extension to find only among that files
#  
# 1. Make list of files in the directory
# 2. Get size of each file and store tuples (file name, size)
# 3. Sort list of tuples by second parameter (size)
# 4. Output the biggest file
