#Q.1 Arithematic operation on two numbers.
#Write a program which accept two integers and display their add,sub,mult,div
from Functions import Addition,Subtraction,Multiplication,Division
def main():
    print("Enter the First Number : ")
    iValue1=int(input())

    print("Enter the Second Number : ")
    iValue2=int(input())

    iRet=Addition(iValue1,iValue2)
    print("Addition of Two Number is : ",iRet)

    iRet=Subtraction(iValue1,iValue2)
    print("Substraction of Two Number is : ",iRet)

    iRet=Multiplication(iValue1,iValue2)
    print("Multiplication of Two Number is : ",iRet)

    iRet=Division(iValue1,iValue2)
    print("Division of Two Number is : ",iRet)

if __name__ == "__main__":
    main()