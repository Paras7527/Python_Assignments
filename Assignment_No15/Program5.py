#Accept file name and one string from user and return the frequency of that string from file
def main():
    print("Enter the File Name that you want :")
    fobj=input()

    print("Enter the String : ")
    str=input()

    fobj=open(fobj,"r")

    fobj=fobj.read()

    iCount=fobj.count(str)
    print("The frequency is :",iCount)

if __name__=="__main__":
    main()