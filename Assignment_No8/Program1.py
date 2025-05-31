#design the python program which creates two thread named as even and odd.Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
import threading
def DisplayEven():
    for i in range(0,21,2):
        print(i)

def DisplayOdd():
    for i in range(1,21,2):
        print(i)
def main():
    T1=threading.Thread(target=DisplayEven)
    T2=threading.Thread(target=DisplayOdd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__=="__main__":
    main()