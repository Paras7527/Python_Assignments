#Write a program which accept N number from user and stored inti list.Return Minimum number from the list.
def Minimum(Data):
    iMin=Data[0]
    for i in Data:
        if i<iMin:
            iMin=i
    return iMin
def main():
    print("Enter the number that you want to accept in list : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    iRet=Minimum(Data)
    print("The minimum number is : ",iRet)

if __name__ == "__main__":
    main()