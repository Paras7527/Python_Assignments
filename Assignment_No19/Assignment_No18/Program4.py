#Write a program which accepts the two file names from user and compare of both the files.If both file contains same content then display the success otherwise display failure.Accept the both file names through command line arg
import sys
import filecmp

def main():
    fobj1=open(sys.argv[1],"r")
    fobj2=open(sys.argv[2],"r")

    FileCompare=filecmp.cmp(sys.argv[1],sys.argv[2])
    if(FileCompare==True):
        print("File Contains the same content!")
    else:
        print("File Doesn't Contains the same content!!!")

if __name__=="__main__":
    main()