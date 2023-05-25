import os



"""
    open(): Opens a file and returns a file object.
close(): Closes the file.
read(): Reads the entire contents of the file as a string.
readline(): Reads a single line from the file.
readlines(): Reads all lines of the file and returns them as a list.
write(): Writes a string to the file.
writelines(): Writes a list of strings to the file.
seek(): Moves the file position to a specified location.
tell(): Returns the current file position.
exists(): Checks if a file or directory exists.
isfile(): Checks if a path points to a file.
isdir(): Checks if a path points to a directory.
mkdir(): Creates a new directory.
rmdir(): Removes an empty directory.
remove(): Deletes a file.
rename(): Renames a file or directory.
listdir(): Returns a list of files and directories in a directory.
getsize(): Returns the size of a file in bytes.
abspath(): Returns the absolute path of a file or directory.
join(): Joins one or more path components.
walk(): Generates the file names in a directory tree by walking the tree top-down or bottom-up.
    """

def count_and_list_folders(path):
    folder_count = 0
    folder_list = []

    for root, dirs, files in os.walk(path):
        for dir in dirs:
            folder_count += 1
            folder_list.append(os.path.join(root, dir))

    return folder_count, folder_list

# Provide the path to the XYZ folder
folder_path = r'D:\Code_Place\Python-jupyter-notebook\2023'

count, folders = count_and_list_folders(folder_path)

print("Number of subfolders:", count)
print("List of subfolders:")
for folder in folders:
    print(folder)


all_files = os.walk(folder_path)

all_files_list = tuple(all_files)
for root, directories, files in all_files:
    print("Directory:", root)
    print("Subdirectories:", directories)
    print("Files:", files)
    print("---")