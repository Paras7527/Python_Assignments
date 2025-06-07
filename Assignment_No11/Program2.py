#Factorial Using Recursion
#Write a recursive function to calculate factorial of a number.

#factorial(5) → 120
iFact=1
def DisplayFactorial(iNo):
    global iFact
    if(iNo>=1):
        iFact=iFact*iNo
        iNo=iNo-1
        DisplayFactorial(iNo)
    return iFact

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=DisplayFactorial(iValue)
    print("The Factorial of number : ",iRet)

if __name__=="__main__":
    main()