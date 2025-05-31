#Create a Python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread.
import threading
import time

def Display1(iNo):
    for i in range(iNo+1):
        print("For Thread 1 : ",i)
        time.sleep(1.0)

def Display2(iNo):
    for i in range(iNo+1):
        print("For Thread 2 : ",i)
        time.sleep(1.0)

def Display3(iNo):
    for i in range(iNo+1):
        print("For Thread 3 : ",i)
        time.sleep(1.0)
def main():

    T1=threading.Thread(target=Display1,args=(5,))
    T2=threading.Thread(target=Display2,args=(5,))
    T3=threading.Thread(target=Display3,args=(5,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__=="__main__":
    main()