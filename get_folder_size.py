import os


def get_folder_size(path_to_folder):
    """
    Total size of the folder.
    One argument: path_to_folder.
    """
    total_size = 0
    for filename in os.listdir(path_to_folder):
        if os.path.isdir(os.path.join(path_to_folder, filename)):
            total_size += get_folder_size(os.path.join(path_to_folder, filename))
            continue
        total_size += os.path.getsize(os.path.join(path_to_folder, filename))
    return total_size


if __name__ == "__main__":
    path_to_folder = input('Enter path to folder => ')
    print(f'Total size of the folder: <{os.path.basename(path_to_folder)}> =>')
    print(f'{get_folder_size(path_to_folder)}') 
