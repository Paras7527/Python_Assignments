#Write a program which accept one number from user and check whether the number is prime or not
def CheckPrime(iNo):
    if(iNo<=1):
        return False
    for i in range(2,iNo):
        if(iNo%i==0):
            return False
    return True

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=CheckPrime(iValue)
    if(iRet==True):
        print("Number is Prime")
    else:
        print("Number is not Prime")
    

if __name__=="__main__":
    main()