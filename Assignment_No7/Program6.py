#return list using prime number
def CheckPrime(iNo):
    if iNo <= 1:
        return False
    for i in range(2, iNo):
        if iNo % i == 0:
            return False
    return True
def main():
    print("Enter the Number :")
    iValue=int(input())

    Data=list()
    print("Enter the Numbers : ")

    for i in range(iValue):
        No=int(input())
        Data.append(No)

    FData=list(filter(CheckPrime,Data))
    print("Filter Data is : ",FData)
    
if __name__=="__main__":
    main()