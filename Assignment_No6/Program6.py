def Displaypattern(iNo):
    for i in range(1,iNo+1):
        for j in range(1,i+1):
            print("*",end="  ")
        print()

def main():
    print("Enter a number: ")
    iValue = int(input())

    Displaypattern(iValue)

if __name__ == "__main__":
    main()


