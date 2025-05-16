#Area and perimeter of reactangle
from Functions import Area,Perimeter

def main():
    print("Enter the Length of Rectangle : ")
    iValue1=int(input())

    print("Enter the Width of Rectangle : ")
    iValue2=int(input())

    iRet=Area(iValue1,iValue2)
    print("Area of Rectangle : ",iRet)

    iRet=Perimeter(iValue1,iValue2)
    print("Perimeter of Rectangle : ",iRet)

if __name__ == "__main__":
    main()