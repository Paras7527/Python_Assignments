#Write a program which display first 10 even numbers on screen.
def DisplayEven(iNo):
    for i in range(0,iNo,2):
        print(i,end="    ")
def main():
    print("Enter the Number")
    iValue=int(input())
    
    DisplayEven(iValue)
if __name__ == "__main__":
    main()