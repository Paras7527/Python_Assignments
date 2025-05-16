#Write a program whic accept N number from user and stored inti list.Return addition of all the elements from the list.
def ListAddition(Data):
    iSum=0
    for i in Data:
        iSum=iSum+i
    return iSum
def main():
    print("Enter the number that you want to accept in list : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    iRet=ListAddition(Data)
    print("Addition of List is : ",iRet)

if __name__ == "__main__":
    main()