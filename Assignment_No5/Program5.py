#Even or Odd Number Check
from Functions import CheckEvenOdd
    
def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=CheckEvenOdd(iValue)
    if(iRet==True):
        print("The Number if Even")
    else:
        print("The Number is Odd")

if __name__=="__main__":
    main()