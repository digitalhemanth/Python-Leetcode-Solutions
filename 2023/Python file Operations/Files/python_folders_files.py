import os

def count_and_list_folders(path):
    folder_count = 0
    folder_list = []

    for root, dirs, files in os.walk(path):
        for dir in dirs:
            folder_count += 1
            folder_list.append(os.path.join(root, dir))

    return folder_count, folder_list

# Provide the path to the XYZ folder
folder_path = '/path/to/XYZ'

count, folders = count_and_list_folders(folder_path)

print("Number of subfolders:", count)
print("List of subfolders:")
for folder in folders:
    print(folder)


