#Write a program that accepts the file name from user and open that file and display the contents of that file on screen

def main():
    print("Enter the name of File :")
    FileName=input()

    fobj=open(FileName,"r")

    fobj=fobj.read()

    print("The Content which File contain is : ",fobj)
    
if __name__=="__main__":
    main()