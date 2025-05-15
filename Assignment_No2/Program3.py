#Write a program which aceept one number from user and returm its factroial.
def Factorial(iNo):
    fact=1
    for i in range(iNo+1):
        fact=fact*i
    return fact
    
def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=Factorial(iValue)
    print("Factorial of Number :",iRet)

if __name__=="__main__":
    main()