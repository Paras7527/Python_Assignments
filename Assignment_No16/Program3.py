#Write a python script to count the number of lines, words, charcters in given file
def main():
    fobj=open("data.txt","r")

    fobj=fobj.read()

    fobj1=len(fobj)                             #Characters 
    print("The Number of characters are : ",fobj1)

    fobj2=len(fobj.split())                     #Words
    print("The Number of Words are : ",fobj2)

    fobj3=len(fobj.splitlines())                #Lines
    print("The Number of Lines are : ",fobj3)


if __name__=="__main__":
    main()