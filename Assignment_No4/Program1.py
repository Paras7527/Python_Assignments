#Write a program which contains one lambda function which accept one parameter and return the power of two

Power = lambda X : X*X

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=Power(iValue)
    print("Power is : ",iRet)

if __name__ == "__main__" : 
    main()