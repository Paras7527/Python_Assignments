#Write a program which contains filter(), map(), reduce() in it.Python application which contains one list of numbers. List contains the number which are accepted from user.
#Filter should filter out all such a numbers which are even.
#Map function will calculate its square
#Reduce will return addition of all that number.
from functools import reduce

DisplayEven = lambda iNo : iNo%2==0

DisplaySquare = lambda iNo : iNo*iNo

DisplayAdd = lambda iNo1,iNo2 : iNo1+iNo2

def main():
    print("Enter the Number : ")
    iValue=int(input())

    Data=list()

    print("Enter the numbers : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    print("Data is : ",Data)

    FData=list(filter(DisplayEven,Data))
    print("Filter Data : ", FData)

    MData=list(map(DisplaySquare,FData))
    print("Map Data : ",MData)

    RData=reduce(DisplayAdd,MData)
    print("Reduce Data : ",RData)

    
if __name__ == "__main__" :
    main()