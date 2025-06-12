#Write a program which accept file name from user and check whether file is present in current directory or not
import os

def main():
    print("Enter the File Name that you want : ")
    Fobj=input()

    Fobj=os.path.exists(Fobj)
    if(Fobj==True):
        print("File is present in Current Directory")
    else:
        print("File is not prsent in Current Directory")

if __name__=="__main__":
    main()