#Sum of n natural numbers
i = 1
sum = 0
def SumNatural(number):
    global sum , i

    if(i <= number ):
        sum = sum + i
        i = i + 1
        SumNatural(number)

    return sum

def main():
    print("Enter the Digit : ")
    iValue=int(input())

    iRet=SumNatural(iValue)
    print("The Sum of natural numbers : ",iRet)


if __name__=="__main__":
    main()