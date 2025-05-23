#Print sum of even numbers between 1 to 100. Use a loop to find and print the sum of all even numbers from 1 to 100.
def SumEven(iNo):
    iSum=0
    for i in range(0,iNo+1,2):
        iSum=iSum+i
    return iSum

def main():
    print("Enter the Number : ")
    iValue = int(input())

    iRet=SumEven(iValue)
    print("Summation is :",iRet)

if __name__ == "__main__":
    main()