import os
import collections

# Find downlaods folder
DOWNLOADS_PATH = os.path.join(
    os.path.expanduser('~'),
    'Downloads'
)

# File type to folder
file_mappings = collections.defaultdict()
for filename in os.listdir(DOWNLOADS_PATH):
    if not os.path.isdir(os.path.join(DOWNLOADS_PATH, filename)):
        file_type = filename.split('.')[-1]
        file_mappings.setdefault(file_type, []).append(filename)

# Move all files into their folder
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(DOWNLOADS_PATH, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_item in folder_items:
        source = os.path.join(DOWNLOADS_PATH, folder_item)
        destination = os.path.join(folder_path, folder_item)
        print(f'Moviendo {source} a {destination}')
        os.rename(source, destination)
