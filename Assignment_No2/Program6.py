#Write a program which accept number and display below pattern
#   1 1 1 1 1           1,1  1,2  1,3  1,4  1,5
#   1 1 1 1             2,1  2,2  2,3  2,4  2,5  
#   1 1 1               3,1  3,2  3,3  3,4  3,5
#   1 1                 4,1  4,2  4,3  4,4  4,5
#   1                   5,1  5,2  5,3  5,4  5,5
def DisplayPattern(iNo):
    for i in range(iNo):
        for j in range(iNo):
            if(i<=j):
                print("*",end="  ")
        print("\n")


def main():
    print("Enter the Number : ")
    iValue=int(input())

    DisplayPattern(iValue)

if __name__=="__main__":
    main()