#Write a program which accept the file name from user and open that file and display the contents of that file screen

def main():
    print("Enter the File Name : ")
    fobj=input()

    fobj=open(fobj,"r")

    fobj=fobj.read()

    print("Contents From file : ",fobj)

if __name__=="__main__":
    main()