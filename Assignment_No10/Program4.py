#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204

from functools import reduce

DisplayEven = lambda iNo : iNo%2==0

DisplaySquare = lambda iNo : iNo*iNo

DisplayAddition = lambda iNo1 , iNo2 : iNo1 + iNo2

def main():
    Data=list()

    print("Enter the element that you want : ")
    iValue=int(input())

    print("The values are : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    fData=list(filter(DisplayEven,Data))
    print("FData is : ",fData)

    mData=list(map(DisplaySquare,fData))
    print("MData is : ",mData)

    rData=reduce(DisplayAddition,mData)
    print("RData is : ",rData)

if __name__=="__main__":
    main()