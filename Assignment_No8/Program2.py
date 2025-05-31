#Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as “exit from main”.
import threading
def EvenFactor(iNo):
    isum=0
    for i in range(2,iNo+1,2):
        if(iNo%i==0):
            isum=isum+i
    print(isum)
            


def OddFactor(iNo):
    isum=0
    for i in range(1,iNo+1,2):
        if(iNo%i==0):
            isum=isum+i
    print(isum)

def main():

    T1=threading.Thread(target=EvenFactor,args=(12,))
    T2=threading.Thread(target=OddFactor,args=(12,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit From Main!!!")

if __name__=="__main__":
    main()