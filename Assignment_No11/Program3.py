#Sum of Digits
#Write a recursive function to calculate the sum of digits of a number.

#sum_of_digits(1234) → 10
iSum=0
def SumDigits(iNo):
    global iSum
    iDigit=0
    if(iNo!=0):
        iDigit=iNo%10
        iNo=iNo//10
        iSum=iSum+iDigit
        SumDigits(iNo)
    return iSum
def main():
    print("Enter the Digit : ")
    iValue=int(input())

    iRet=SumDigits(iValue)
    print("Sum of the Digits : ",iRet)

if __name__=="__main__":
    main()