#Accept the list from user and use filter() to keep even numbers only
KeepEven=lambda iNo:(iNo%2)==0
def main():
    print("Enter the Number :")
    iValue=int(input())

    Data=list()
    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    FData=list(filter(KeepEven,Data))
    print("Filter Data is : ",FData)
    
if __name__=="__main__":
    main()