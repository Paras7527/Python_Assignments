#Print Numbers Using Recursion
#Write a recursive function to print numbers from 1 to N.

#Expected Output (for n=5):
#1 2 3 4 5
iCnt=1
def Display(iNo):
    global iCnt
    if(iCnt<=iNo):
        print(iCnt)
        iCnt=iCnt+1
        Display(iNo)

def main():
    print("Enter the Number : ")
    iValue=int(input())

    iRet=Display(iValue)
    print("It Shows : ",iRet)

if __name__=="__main__":
    main()
