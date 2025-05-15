#Write a program which accept number and display below number
def Display(No):
    for i in range(No):
        for j in range(No):
            print("*",end="  ")
        print("\n")
def main():
    print("Enter the Number")
    iValue=int(input())

    Display(iValue)

if __name__ == "__main__":
    main()