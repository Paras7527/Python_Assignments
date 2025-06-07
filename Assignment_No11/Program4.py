#Power Function Using Recursion
#Write a recursive function to calculate x^n.

#power(2, 3) → 8

def DisplayPower(iNo1,iNo2):
    if(iNo2==0):
       return 1
    return iNo1*DisplayPower(iNo1,iNo2-1)
    
def main():
    print("Enter the Base number : ")
    iValue1=int(input())

    print("Enter the Exponant : ")
    iValue2=int(input())

    iRet=DisplayPower(iValue1,iValue2)
    print("Power : ",iRet)

if __name__=="__main__":
    main()