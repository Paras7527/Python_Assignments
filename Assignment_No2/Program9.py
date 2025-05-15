#Write a program which accept one number from user and return the number of digits in the numbers.
def CountDigit(iNo):
    iCount=0
    if iNo==0:
        return 1
    
    if iNo<0:
        iNo=-iNo
        
    while(iNo!=0):
        iNo=iNo//10
        iCount=iCount+1
    return iCount

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=CountDigit(iValue)
    print("Digits are : ",iRet)
    
if __name__=="__main__":
    main()