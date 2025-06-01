#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000
from functools import reduce

DisplayRange=lambda iNo : iNo>=70 and iNo<=90

Increase=lambda iNo : iNo + 10

DisplayProduct=lambda iNo1,iNo2:iNo1*iNo2

def main():
    Data=list()

    print("Enter the element that you want : ")
    iValue=int(input())

    print("The values are : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    fData=list(filter(DisplayRange,Data))
    print("FData is : ",fData)

    mData=list(map(Increase,fData))
    print("MData is : ",mData)

    rData=reduce(DisplayProduct,mData)
    print("RData is : ",rData)

if __name__=="__main__":
    main()