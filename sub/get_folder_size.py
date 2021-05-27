import os


def get_folder_size(path_to_folder):
    """
    Total size of the folder.
    """
    total_size = 0
    for filename in os.listdir(path_to_folder):
        if os.path.isdir(os.path.join(path_to_folder, filename)):
            total_size += get_folder_size(os.path.join(path_to_folder, filename))
            continue
        total_size += os.path.getsize(os.path.join(path_to_folder, filename))
    return total_size

def folder_size2(folder_path):
    total = 0
    for cur_dir, sub_dirs, list_files in os.walk(folder_path):
        for f in list_files:
            total += os.path.getsize(os.path.join(cur_dir, f))
    return total


if __name__ == "__main__":
    path_to_folder = input('Enter path to folder => ')
    print(f'Total size of the folder: <{os.path.basename(path_to_folder)}> =>')
    fldr_size = get_folder_size(path_to_folder)
    print(f'{fldr_size}')
    fldr_size_2 = folder_size2(path_to_folder) 
    print(f'Total size of the folder with os.walk func => {fldr_size_2}')
    print(fldr_size == fldr_size_2)
    

