#Write a program to read a file line by line and display on thoes lines that contains more than 5 words

def main():
    fobj=open("Program5.txt","r")

    fobj=fobj.read()
    
    value=fobj.split()

    for i in value:
        if len(i)>5:
            print(i)

if __name__=="__main__":
    main()