import os
import sys
import time
import hashlib
def FileExtension(directory,extension):
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)
    return found_files

def CalculateCheckSum(path,BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def Directorywatcher(DirectoryName="Marvellous"):

    Flag = os.path.isabs(DirectoryName)

    if(Flag == False):
        DirectoryName=os.path.abspath(DirectoryName)

    Flag=os.path.exists(DirectoryName)
    if(Flag==False):
        print("The path is invalid")
        exit()

    Flag=os.path.isdir(DirectoryName)
    if(Flag==False):
        print("Path is valid but target is not a directory")
        exit()

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)
            print("File name : ",fname)
            print("CheckSum : ",checksum)
            print()

    timestam=time.ctime()       #overall time

    Border="-" * 51

    FileName="MarvellousLog%s.log" %(timestam)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")

    print(FileName)

    fobj=open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file of marvellous automations script\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at : \n"+timestam+"\n")
    fobj.write(Border+"\n")

def FindDuplicate(DirectoryName="Marvellous"):

    Flag = os.path.isabs(DirectoryName)

    if(Flag == False):
        DirectoryName=os.path.abspath(DirectoryName)

    Flag=os.path.exists(DirectoryName)
    if(Flag==False):
        print("The path is invalid")
        exit()

    Flag=os.path.isdir(DirectoryName)
    if(Flag==False):
        print("Path is valid but target is not a directory")
        exit()

    Duplicate={}

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum]=[fname]

    return Duplicate

def main():
    Border="-"*51
    print(Border)                                                       
    print("-------------Marvellous Automation-----------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform Directory Cleaning")
            print("This is the Directory Automation script")
        
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as .........")
            print("ScriptName.py  NameofDirectory")
            print("Please provide valid absolute path")

    elif len(sys.argv) == 3:
        directory = sys.argv[1]
        extension = sys.argv[2]

        if not os.path.exists(directory):
            print("Error: The given directory does not exist.")
            exit()

        if not os.path.isdir(directory):
            print("Error: The given path is not a directory.")
            exit()

        if not extension.startswith('.'):
            print("Error: Extension should start with a dot (e.g., .txt)")
            exit()

        result = FileExtension(directory, extension)

        if result:
            print(f"\nFiles found with '{extension}' extension:\n")
            for file in result:
                print(file)
        else:
            print(f"No files found with '{extension}' extension.")

    else:
        print("Invalid Number of Command Line Arguments!!!")
        print("Use the given flags as : ")
        print("--h : Used to Display the Help")
        print("--u : Used to Display the Usage")

    print(Border)
    print("-----------Thank for using our script--------------")
    print("-------------Marvellous Infosystems----------------")
    print(Border)

if __name__=="__main__":
    main()

