#Accept the list from user and use reduce() to find the product of all the number
from functools import reduce
DisplayProduct = lambda iNo1,iNo2 : iNo1*iNo2

def main():
    print("Enter the Number :")
    iValue=int(input())

    Data=list()
    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    RData=reduce(DisplayProduct,Data)
    print("Filter Data is : ",RData)
    
if __name__=="__main__":
    main()