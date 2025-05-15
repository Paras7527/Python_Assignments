#Write a program which accept one number from user and return the addtion of its factor
def SumFactors(iNo):
    iSum=0
    for i in range(1,iNo):
        if((iNo%i)==0):
            iSum=iSum+i
    return iSum
    
def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=SumFactors(iValue)
    print("Factors are:",iRet)
    

if __name__=="__main__":
    main()