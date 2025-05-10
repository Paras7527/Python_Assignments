#Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is Even then it should display "Even Number" otherwise display "Odd Number" on console.
def ChkNum(iNo):
    if((iNo%2)==0):
        return True
    else:
        return False
    
def main():
    print("Enter the Number : ")
    iValue=int(input())
    
    iRet=ChkNum(iValue)
    if(iRet == True):
        print("The Number is Even")
    else:
        print("The Number is Odd")
    
if __name__ == "__main__":
    main()