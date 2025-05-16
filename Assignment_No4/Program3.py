#Write a program which contains filter(), map(), reduce() in it.Python application which contains one list of numbers. List contains the number which are accepted from user.
#Filter should filter out all such a numbers which greater than or equal to 70 and less than or equal to 90.
#Map function will increase each number by 10
#Reduce will return prouct of all that number.
from functools import reduce

Display = lambda iNo : iNo>=70 and iNo<=90

Increase = lambda iNo : iNo+10

Multiplication = lambda iNo1,iNo2 : iNo1*iNo2

def main():
    print("Enter the Number : ")
    iValue=int(input())

    Data=list()

    print("Enter the numbers : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)

    print("Data is : ",Data)

    FData=list(filter(Display,Data))
    print("Filter Data : ", FData)

    MData=list(map(Increase,FData))
    print("Map Data : ",MData)

    RData=reduce(Multiplication,MData)
    print("Reduce Data : ",RData)

    
if __name__ == "__main__" :
    main()