#Write a program which contains one function that accept one number from user and return true if number is divisible by 5 otherwise return false.
def ChkDivisible(iNo):
    if((iNo%5)==0):
        return True
    else:
        return False

def main():
    print("Enter the Number : ")
    iValue=int(input())
    
    iRet=ChkDivisible(iValue)
    if(iRet==True):
        print("The Number is Divisible by 5")
    else:
        print("The Number is not Divisible by t")
    
if __name__ == "__main__":
    main()