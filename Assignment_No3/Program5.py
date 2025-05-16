#Write a program which accept one number from user and stored into the list.Return addition of all the prime numbers from that list.
from PrimeNum import CheckPrime

def main():
    print("Enter the number of elements you want to enter:")
    iValue = int(input())

    Data = ()

    print("Enter the numbers:")
    for i in range(iValue):
        No = int(input())
        Data.append(No)

    iSum = 0
    for num in Data:
        if CheckPrime(num):
            iSum =iSum + num

    print("Addition of all prime numbers is:", iSum)

if __name__ == "__main__":
    main()
