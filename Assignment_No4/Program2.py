#Write a program which contains one lambda function which accept one parameter and return its multiplication

Power = lambda X,Y : X*Y

def main():
    print("Enter the First Number : ")
    iValue1=int(input())

    print("Enter the Second Number : ")
    iValue2=int(input())

    iRet=Power(iValue1,iValue2)
    print("Power is : ",iRet)

if __name__ == "__main__" : 
    main()