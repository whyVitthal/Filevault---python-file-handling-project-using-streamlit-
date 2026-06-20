from pathlib import Path     #importing the pathlib module and giving it an alias 'Path' for easier reference in the code. The pathlib module provides an object-oriented interface for working with file system paths, making it easier to handle file and directory operations in a more intuitive way.
import os                #importing the os module to interact with the operating system, such as file handling and directory operations. while removing the file we need to import os module to use the remove function to delete the file from the system.

def createfile():
    try:
         name=input("enter the file name: ")
         path=Path(name)
         if not path.exists():
            with open(path,"w") as fs:
                data=input("enter the data to be written in the file: ")
                fs.write(" \n" + data)
            print("file created successfully")    
         else:
             print("there is an error file already exists")  
    except Exception as e:
        print(f"there is an error:{e}")

def readfile():
    try:
        name=input("enter the file name: ")
        path=Path(name)
        if path.exists():
            with open(path,"r") as fr:
                data=fr.read()
                print(data)
        else:
            print("there is an error file does not exist")        
    except Exception as e:
        print(f"there is an error:{e}")
def updatefile():
    try:
        name=input("enter the file name: ")
        path=Path(name)
        if path.exists():
            print("operations")
            print("1 . renaming the file")
            print("2 . appending to the file")
            print("3 . overwriting the file")

            choice=int(input("enter your choice; "))
            if choice==1:
                newname = input("enter the new name of the file: ")
                new_path=Path(newname) 
                if not new_path.exists():
                    path.rename(new_path)
                    print("file renamed successfully")
                else:
                    print("there is an error file with the new name already exists")    

            
            elif choice==2:
                with open(path,"a") as fa:
                    data=input("enter the data to be appended to the file:")
                    fa.write(" \n" + data)
                    print("data appended successfully")

            elif choice==3: 
                with open(path,"w") as fw:
                    data=input("enter the data to be written in the file: ")
                    fw.write(" \n "+data)
                    print("file overwritten successfully")
    except Exception as e:
        print(f"there is an error:{e}")

def deletefile():
    try:
        name=input("enter the file name: ")
        path=Path(name)
        if path.exists():
            path.unlink() #os.remove(path)
            print("file deleted successfully")
        else:
            print("there is an error file does not exist")
    except Exception as e:
        print(f"there is an error:{e}")        

print("press 1 to create a file")
print("press 2 to read a file")
print("press 3 to update a file")
print("press 4 to delete a file")

a=int(input("enter your choice: "))

if a==1:
    createfile()
if a==2:
    readfile()    
if a==3:
    updatefile()
if a==4:
    deletefile()