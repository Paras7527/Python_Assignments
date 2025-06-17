#Write a program which accepts file name from user and check whether the file exists in current directory or not
import os

def main():
    print("Enter the Name of File That you want to check")
    FileName=input()

    if(os.path.exists(FileName)):
        print("File Exists in the current directory!")
    else:
        print("File is not there!!!")

if __name__=="__main__":
    main()