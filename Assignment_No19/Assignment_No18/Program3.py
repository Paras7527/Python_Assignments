#Write a program which accepts the file name from user and create the new file named as Demo.txt and copy all the contents from existing file into new file .Accept the file name through command line arguments
import sys

def main():
    FileName1=sys.argv[1]

    fobj1=open(FileName1,"r")

    print("Enter the File Name :")
    FileName2=input()

    fobj2=open(FileName2,"w")
    
    fobj2.write(fobj1.read())
    
if __name__=="__main__":
    main()