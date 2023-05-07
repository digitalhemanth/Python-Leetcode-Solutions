import os
import shutil
import datetime


class Folder:
    def create_folder(self, folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")

    def select_folder(self, folder_name):
        os.chdir(folder_name)
        print(f"Selected folder: {os.getcwd()}")

    def delete_folder(self, folder_name):
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")

    def copy_files(self, source_folder, destination_folder):
        shutil.copytree(source_folder, destination_folder)
        print(f"Files copied from '{source_folder}' to '{destination_folder}' successfully.")

    def list_files_and_folders(self):
        contents = os.listdir()
        print("Files and folders in the current directory:")
        for item in contents:
            print(item)


class File:
    def create_file(self, file_name):
        with open(file_name, "w") as file:
            print(f"File '{file_name}' created successfully.")

    def update_file(self, file_name):
        content = input("Enter the content to append to the file: ")
        with open(file_name, "a") as file:
            file.write(content)
        print(f"Content appended to file '{file_name}' successfully.")

    def get_file_details(self, file_name):
        file_stats = os.stat(file_name)
        created_time = datetime.datetime.fromtimestamp(file_stats.st_ctime)
        modified_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)
        file_size = file_stats.st_size

        print("File details:")
        print(f"File name: {file_name}")
        print(f"Created time: {created_time}")
        print(f"Modified time: {modified_time}")
        print(f"File size: {file_size} bytes")

    def delete_file(self, file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")


# Usage example
folder = Folder()
file = File()

while True:
    print("Menu:")
    print("1. Folder operations")
    print("2. File operations")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        folder_option = input("Folder operations: 1. Create folder, 2. Select folder, 3. Delete folder, 4. Copy files, 5. List files and folders: ")

        if folder_option == "1":
            folder_name = input("Enter the folder name to create: ")
            folder.create_folder(folder_name)
        elif folder_option == "2":
            folder_name = input("Enter the folder name to select: ")
            folder.select_folder(folder_name)
        elif folder_option == "3":
            folder_name = input("Enter the folder name to delete: ")
            folder.delete_folder(folder_name)
        elif folder_option == "4":
            source_folder = input("Enter the source folder: ")
            destination_folder = input("Enter the destination folder: ")
            folder.copy_files(source_folder, destination_folder)
        elif folder_option == "5":
            folder.list_files_and_folders()
        else:
            print("Invalid option.")

    elif option == "2":
        file_option = input("File operations: 1. Create file, 2. Update file, 3. Get file details, 4. Delete file: ")

        if file_option == "1":
            file_name = input("Enter the file name to create: ")
            file.create_file(file_name)
        elif file_option == "2":
            file_name = input("Enter the file name to update: ")
            file.update_file(file_name)
        elif file_option == "3":
            file_name = input("Enter the file name to get details: ")
            file.get_file_details(file_name)
        elif file_option == "4":
            file_name = input("Enter the file name to delete: ")
            file.delete_file(file_name)
        else:
            print("Invalid option.")

    elif option == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid option.")

