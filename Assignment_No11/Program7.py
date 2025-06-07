#Print Pattern
def DisplayPattern(iRow,iCol=0):
    if iRow==0:
        return 
    if iCol<iRow:
        print("*",end="  ")
        DisplayPattern(iRow,iCol+1)
    else:
        print()
        DisplayPattern(iRow-1,0)

def main():
    print("Enter the Digit : ")
    iValue=int(input())

    DisplayPattern(iValue,0)

if __name__=="__main__":
    main()