#Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.
import threading

def CountSmall(mystr):
    iCount=0
    for i in range(len(mystr)):
        ch=mystr[i]
        if(ch>='a' and ch<='z'):
            iCount=iCount+1
    
    print("Number of small characters are : ",iCount , " ID is : ",threading.get_ident(),"Name of thread is : ",threading.current_thread().name)

def CountCapital(mystr):
    iCount=0
    for i in range(len(mystr)):
        ch=mystr[i]
        if(ch>='a' and ch<='z'):
            iCount=iCount+1
    
    print("Number of Capital characters are : ",iCount , " ID is : ",threading.get_ident(),"Name of thread is : ",threading.current_thread().name)

def CountDigits(mystr):
    iCount=0
    for i in range(len(mystr)):
        ch=mystr[i]
        if(ch>='0' and ch<='9'):
            iCount=iCount+1
    
    print("Number of Digits are : ",iCount , " ID is : ",threading.get_ident(),"Name of thread is : ",threading.current_thread().name)

def main():
    small=threading.Thread(target=CountSmall,args=("PAras",))
    capital=threading.Thread(target=CountCapital,args=("PAras",))
    digits=threading.Thread(target=CountDigits,args=("PAras12345",))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

if __name__=="__main__":
    main()