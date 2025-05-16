#Celcius to Farhenite Converter:
from Functions import CheckTemp

def main():
    print("Enter the Temperature in Celcius : ")
    fValue=float(input())

    fRet=CheckTemp(fValue)
    print("The Temperature in farenheit is : ",fRet,"°F")

if __name__ == "__main__":
    main()