#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62
from functools import reduce

def CheckPrime(iNo):
    if iNo <= 1:
        return False
    for i in range(2, int(iNo ** 0.5) + 1):
        if iNo % i == 0:
            return False
    return True

Display = lambda iNo : iNo*2

DisplayMax = lambda iNo1 , iNo2 : iNo1 if(iNo1>iNo2) else iNo2

def main():
    Data=list()

    print("Enter the element that you want : ")
    iValue=int(input())

    print("The values are : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    fData=list(filter(CheckPrime,Data))
    print("FData is : ",fData)

    mData=list(map(Display,fData))
    print("MData is : ",mData)

    rData=reduce(DisplayMax,mData)
    print("RData is : ",rData)

if __name__=="__main__":
    main()