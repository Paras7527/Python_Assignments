#Write a program which contains one lambda function which accepts two parameters and return its multiplication.

#Input : 4  3    Output : 12
#Input : 6  3    Output : 18

Multi = lambda iNo1 , iNo2 : iNo1 * iNo2

def main():
    print("Enter the First Number : ")
    iVal1=int(input())

    print("Enter the Second Number : ")
    iVal2=int(input())

    iRet=Multi(iVal1,iVal2)
    print("The Multiplication of Two number is : ",iRet)

if __name__ == "__main__":
    main()