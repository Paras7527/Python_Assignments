#Count Zeros in a Number (Recursively)
#Write a recursive function to count how many zeros are in the given number.

#count_zeros(1020300) → 4
iCount=0
def CountZero(iNo):
    global iCount
    iDigit=0
    if(iNo!=0):
        iDigit=iNo%10
        if(iDigit==0):
            iCount=iCount+1
        iNo=iNo//10
        CountZero(iNo)
    return iCount
def main():
    print("Enter the Digit : ")
    iValue=int(input())

    iRet=CountZero(iValue)
    print("The number of Zeros are : ",iRet)


if __name__=="__main__":
    main()