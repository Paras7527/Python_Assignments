#Accept the list of Integers from the user and use the map() fun to double each value
List=lambda iNo : iNo*2

def main():
    
    print("Enter the Number that you want to stored in list : ")
    iValue=int(input())

    Data=list()

    print("Enter the Numbers : ")
    for i in range(iValue):
        No=int(input())
        Data.append(No)    

    print("The Data is : ",Data)
    MData=list(map(List,Data))
    print("The Map Data is : ",MData)
    
if __name__=="__main__":
    main()