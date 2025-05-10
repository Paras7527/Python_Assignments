#Write a program which conatains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
def Add(iNo1,iNo2):
    iAns = iNo1 + iNo2
    return iAns

def main():
    print("Enter the First Number : ")
    iValue1=int(input())
    
    print("Enter the Second Number : ")
    iValue2=int(input())
    
    iRet=Add(iValue1,iValue2)
    print("Addition of Two Numbers are : ",iRet)
    
if __name__ == "__main__":
    main()