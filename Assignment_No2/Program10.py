#Write a program which accept one number from user and return the addition of digits in the numbers.
def CountDigit(iNo):
    iSum=0
    if iNo==0:
        return 1
    
    if iNo<0:
        iNo=-iNo
        
    while(iNo!=0):
        iDigit=iNo%10
        iNo=iNo//10
        iSum=iSum+iDigit
    return iSum

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=CountDigit(iValue)
    print("Digits are : ",iRet)
    
if __name__=="__main__":
    main()