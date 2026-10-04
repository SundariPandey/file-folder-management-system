from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")

def createFile():
    try:
        readFileAndFolder()
        name = input("Please Enter your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Please Tell what you want to write this file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY!")

        else:
            print("This file already exist.")
    except Exception as err:
        print(f"An error occured {err}")

def readFile():
    try:

        readFileAndFolder()
        name = input("Which file you want to read please write your file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("READED SUCCESSFULLY!")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f"An error occured {err}")



def updateFile():
    try:
        readFileAndFolder()
        name = input("Which file you want update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1: Rename the file")
            print("Press 2: Overwrite the file")
            print("Press 3: Append content to the file")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter your new File name: ")
                new_path = Path(new_name)
                p.rename(new_path)
                print("Rename Successfully!")
        
            elif choice == 2:
                with open(p,"w") as fs:
                    data = input("Write your data which you want to overwrite in your file: ")
                    fs.write(data)
                print("Overwrite Sucessfully!")

            elif choice == 3:
                with open(p,"a") as fs:
                    data = input("Please write What you want to add in your file: ")
                    fs.write(" "+data)
                print("Content Added Successfullly!")
        
            else:
             print("Invalid choice. Please choose between 1, 2, and 3.")

        else:
            print("File doesn't exists.")

    except Exception as err:
        print(f"An error occured {err}")

def delFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print("File Remove Successfully!")
        else:
            print("File doesn't exist.")
    except Exception as err:
        print(f"An error occured {err}")


def createFolder():
    try:

        readFileAndFolder()

        name = input("Enter your folder name: ")
        p = Path(name)

        if not p.exists():
            p.mkdir()
            print("FOLDER CREATED SUCCESSFULLY!")
        else:
            print("FOLDER ALREADY EXISTS")

    except Exception as err:
        print(f"An error occured {err}")

def viewFolder():

    try:
        readFileAndFolder()
        name = input("Which folder do you want to view: ")
        p = Path(name)

        if p.exists() and p.is_dir():
            # yahan folder ke andar ke items nikalne hain
            items = list(p.iterdir())

            for i,item in enumerate(items):
                print(f"{i+1} : {item}")

        else:
            print("Folder does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")


def createFileInFolder():
    try:
        folder_name = input("Enter folder name: ")
        p = Path(folder_name)

        if p.exists() and p.is_dir():

            file_name = input("Enter file name: ")
            file_path = p / file_name

            if not file_path.exists():
                with open(file_path, "w") as fs:
                    data = input("Enter your content: ")
                    fs.write(data)

                print("FILE CREATED INSIDE FOLDER SUCCESSFULLY!")
            else:
                print("File already exists.")

        else:
            print("Folder does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")

def renameFolder():

    try:
        readFileAndFolder()
        name = input("Enter your folder name which you want to rename: ")
        p = Path(name)

        if p.exists() and p.is_dir():
            folder_new_name = input("Enter New Folder Name: ")
            folder_new_path = Path(folder_new_name)
            

            if not folder_new_path.exists():
                p.rename(folder_new_path)
                print("RENAME SUCCESSFULLY!")
            else:
                print("A folder or file with this name already exists.")
        else:
            print("Folder does'nt exist.")

    except Exception as err:
        print(f"An error accurred: {err}")


def deleteFolder():
    try:
        readFileAndFolder()

        name = input("Which folder do you want to delete? ")
        p = Path(name)

        if p.exists() and p.is_dir():
            p.rmdir()
            print("FOLDER DELETED SUCCESSFULLY!")

        else:
            print("Folder does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")
            


# Main Menu

def main():
    while True:

        print("\n------------------------------")
        print("       FILE MANAGER")
        print("------------------------------")

        print("Press 1: CREATE FILE")
        print("Press 2: READ FILE")
        print("Press 3: UPDATE FILE")
        print("Press 4: DELETE FILE")
        print("Press 5: CREATE FOLDER")
        print("Press 6: VIEW FOLDER")
        print("Press 7: CREATE FILE IN FOLDER")
        print("Press 8: RENAME FOLDER")
        print("Press 9: DELETE FOLDER")
        print("Press 10: EXIT")

        try:
         choice = int(input("Enter your choice: "))
        except ValueError:
         print("Please enter a number.")
         continue

        if choice == 1:
            createFile()

        elif choice == 2:
            readFile()

        elif choice == 3:
            updateFile()

        elif choice == 4:
            delFile()

        elif choice == 5:
            createFolder()

        elif choice == 6:
            viewFolder()

        elif choice == 7:
            createFileInFolder()

        elif choice == 8:
            renameFolder()

        elif choice == 9:
            deleteFolder()

        elif choice == 10:
            print("Thank you! Program closed.")
            break

        else:
            print("Invalid choice. Please choose between 1 and 10.")

if __name__ == "__main__":
    main()