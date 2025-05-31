#Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.
import multiprocessing

def DisplayFactorial(iNo):
    iFact=1
    for i in range(1,iNo+1):
        iFact=iFact*i
    return iFact

def main():
    Data=list()

    print("Enter the Size of List : ")
    Value=int(input())

    print("Enter the Numbers : ")
    for i in range(Value):
        No=int(input())
        Data.append(No)

    result=[]

    p=multiprocessing.Pool()
    result=p.map(DisplayFactorial,Data)

    print("Square is : ",result)


if __name__=="__main__":
    main()