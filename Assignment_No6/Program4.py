# Function to calculate factorial of a number
def Fact(iNo):
    result = 1
    for i in range(1, iNo + 1):
        result=result * i
    return result

def main():
    print("Enter the number : ")
    iValue = int(input())

    iRet=Fact(iValue)
    print(iRet)



if __name__ == "__main__":
    main()
