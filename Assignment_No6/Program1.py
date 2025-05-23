#Write a program using while loop to print numbers 1 to 50
def Display(iNo):
    i=1
    while(i<=iNo):
        print(i,end=" ")
        i=i+1
def main():
    print("Enter the Number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()