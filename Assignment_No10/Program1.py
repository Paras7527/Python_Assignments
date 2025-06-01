#Write a program which contains one lambda function which accepts one parameter and return power of two.

#Input : 4    Output : 16
#Input : 6    Output : 64

DisplaySquare=lambda iNo : iNo*iNo

def main():
    print("Enter the number : ")
    iValue=int(input())

    iRet=DisplaySquare(iValue)
    print("The Square is : ",iRet)

if __name__=="__main__":
    main()