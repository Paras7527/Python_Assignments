#Check whether prime or not.

def CheckPrime(iNo):
    if iNo <= 1:
        return False
    for i in range(2, int(iNo ** 0.5) + 1):
        if iNo % i == 0:
            return False
    return True

def main():
    print("Enter a number: ")
    iValue = int(input())

    if CheckPrime(iValue):
        print("Number is a prime number.")
    else:
        print("Number is not a prime number.")

if __name__ == "__main__":
    main()


