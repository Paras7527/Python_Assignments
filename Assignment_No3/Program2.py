#Write a program which accept N number from user and stored inti list.Return Maximum number from the list.
def Maximum(Data):
    iMax=Data[0]
    for i in Data:
        if i>iMax:
            iMax=i
    return iMax
def main():
    print("Enter the number that you want to accept in list : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    iRet=Maximum(Data)
    print("The maximum number is : ",iRet)

if __name__ == "__main__":
    main()