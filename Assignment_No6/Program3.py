#Accept Number from user and print multiplication table upto 10
def Multiplication(iNo):
    for i in range(1, 11):
        print(f"{iNo} x {i} = {iNo * i}")


def main():
    print("Enter the Number : ")
    iValue = int(input())

    Multiplication(iValue)

if __name__ == "__main__":
    main()