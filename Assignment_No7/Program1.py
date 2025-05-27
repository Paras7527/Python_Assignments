#Write two lambda fun 1)Square 2)Cube
Square=lambda iNo : iNo*iNo

Cube=lambda iNo :iNo**iNo

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=Square(iValue)
    print("The Square is : ",iRet)
    iRet=Cube(iValue)
    print("The Cube is : ",iRet)


if __name__=="__main__":
    main()