#Write a program which contains filter(), map(), reduce() in it.Python application which contains one list of numbers. List contains the number which are accepted from user.
#Filter should filter out all prime numbers.
#Map function will multiply each number with 2.
#Reduce will return maximum number from that list.
from functools import reduce

def CheckPrime(iNo):
    if(iNo<=1):
        return False
    for i in range(2,iNo):
        if(iNo%i==0):
            return False
    return True

Multi = lambda iNo : iNo*2

Maximum = lambda iNo1,iNo2 : iNo1 if iNo1>iNo2 else iNo2

def main():
    print("Enter the Number : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    print("Data is : ",Data)

    FData=list(filter(CheckPrime,Data))
    print("Filter Data : ",FData)

    MData=list(map(Multi,FData))
    print("Map Data : ",MData)

    RData=reduce(Maximum,MData)
    print("Reduce Data : ",RData)

if __name__ == "__main__":
    main()