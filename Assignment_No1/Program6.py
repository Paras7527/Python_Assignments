#Write a program which accept number from user and check whether that number is positive or negative or zero.
def ChkNum(iNo):
    if(iNo<0):
        print("Number is Negative")
    elif(iNo==0):
        print("Number is Zero")
    else:
        print("Number is Positive")

def main():
    print("Enter the Number : ")
    iValue=int(input())
    
    ChkNum(iValue)
    
if __name__ == "__main__":
    main()