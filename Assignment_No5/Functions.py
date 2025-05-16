#Program 1
def Addition(iNo1,iNo2):
    Ans=0
    Ans=iNo1+iNo2
    return Ans

def Subtraction(iNo1,iNo2):
    Ans=0
    Ans=iNo1-iNo2
    return Ans

def Multiplication(iNo1,iNo2):
    Ans=0
    Ans=iNo1*iNo2
    return Ans

def Division(iNo1,iNo2):
    Ans=0
    Ans=iNo1/iNo2
    return Ans

#Program2 
def CheckVowels(ch):
    if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
        return True
    else:
        return False
    
#Program 3
def CheckVoteEligibility(Age):
    if(Age<0):
        Age=-Age
    if(Age>=18):
        return True
    else:
        return False
    
#Program 4
def DisplayLargest(iNo1,iNo2,iNo3):
    if(iNo1>iNo2 and iNo1>iNo3):
        return iNo1
    elif(iNo2>iNo3 and iNo2>iNo1):
        return iNo2
    elif(iNo3>iNo1 and iNo3>iNo2):
        return iNo3
    
#Program 5
def CheckEvenOdd(iNo):
    if iNo%2==0:
        return True
    else:
        return False
    
#Program 6
def CheckTemp(Celcius):
    Farhenite=0
    Farhenite=((Celcius * (9 / 5)) + 32)
    return Farhenite

#Program 7
def Area(Length,Width):
    Area=0
    Area=Length*Width
    return Area
def Perimeter(Length,Width):
    Perimeter=0
    Perimeter=(2*(Length+Width))
    return Perimeter