#Find Largest Among Three number
from Functions import DisplayLargest

def main():
    print("Enter First Number : ")
    iValue1=int(input())

    print("Enter Second Number : ")
    iValue2=int(input())

    print("Enter Third Number : ")
    iValue3=int(input())

    iRet=DisplayLargest(iValue1,iValue2,iValue3)
    print("The Largest Number Among Three is : ",iRet)

if __name__ == "__main__":
    main()