#import Calculator 
import Calculator as C

def main():
    print("Enter the First Number : ")
    Value1=int(input())
    
    print("Enter the Second Number : ")
    Value2=int(input())
    
    iRet=C.Addition(Value1,Value2)
    print("Addition of Two Numbers : " , iRet)
    
    iRet=C.Substrction(Value1,Value2)
    print("Substraction of Two Numbers : " , iRet)
    
    iRet=C.Multiplication(Value1,Value2)
    print("Multiplication of Two Numbers : " , iRet)
    
    iRet=C.Division(Value1,Value2)
    print("Division of Two Numbers : " , iRet)
    
if __name__=="__main__":
    main()
