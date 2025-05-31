#Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition#Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as “exit from main”.
import threading
def EvenList(iNo):
    isum=0
    for i in iNo:
        if(i%2==0):
            isum=isum+i
    print(isum)
            


def OddList(iNo):
    isum=0
    for i in iNo:
        if(i%2!=0):
            isum=isum+i
    print(isum)

def main():
    data=[1,2,3,4,5,6,7,8,9,10]

    T1=threading.Thread(target=EvenList,args=(data,))
    T2=threading.Thread(target=OddList,args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__=="__main__":
    main()