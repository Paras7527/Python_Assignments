#Write a Python program using multiprocessing.Process to square a list of numbers using multiple processes.
import multiprocessing

def DisplaySquare(iNo):
    return iNo*iNo

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
    result=p.map(DisplaySquare,Data)

    print("Square is : ",result)


if __name__=="__main__":
    main()