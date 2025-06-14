#Write a program to read and display the contents of file data.txt

def main():
    fobj=open("data.txt","r")

    fobj=fobj.read()
    
    print("The contents from the file data.txt is : ",fobj)


if __name__=="__main__":
    main()