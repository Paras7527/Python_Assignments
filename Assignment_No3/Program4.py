#Write a program whic accept N number from user and stored inti list.Accept one number from user and
#return frequency of that number from that list

def Frequency(Data,iNo):
    iCount=0
    for i in Data:
        if iNo==i:
            iCount=iCount+1
    return iCount

def main():
    print("Enter the number that you want to accept in list : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    print("Enter the Number that you want to check the Frequency : ")
    iCnt=int(input())

    iRet=Frequency(Data,iCnt)
    print("The Frequnecy is : ",iRet)

if __name__ == "__main__":
    main()