import sys
import os

files_list = []

def bigfile(p):
    for cur_dir, sub_dirs, cur_files in os.walk(p):
        for f in cur_files:
            full_path = os.path.join(cur_dir, f)
            size_f = os.path.getsize(full_path)
            files_list.append((full_path, size_f))
            files_list.sort(key=lambda x: x[1], reverse=True)
    return files_list


if __name__ == "__main__":
    path_folder = input('Enter path to folder => ')
    flist = bigfile(path_folder)
    print(flist[:5])
    print()
    print(flist[-5:])
        



# TODO
# The func can recieve a file path from sys.argv or clipboard
# The func can recieve file extension to find only among that files
#  
# 1. Make list of files in the directory
# 2. Get size of each file and store tuples (file name, size)
# 3. Sort list of tuples by second parameter (size)
# 4. Output the biggest file
