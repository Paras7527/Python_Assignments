#Accept the file name and one string fro user and return the frequency of that string from file

def main():
    print("Enter the Name of the file:")
    FileName=input()

    print("Enter the String : ")
    str=input()

    fobj=open(FileName,"r")

    fobj1=fobj.read()

    CountFreq=fobj1.count(str)
    print("Enter the Frequency of given string is : ",CountFreq)

    fobj.close()

if __name__=="__main__":
    main()