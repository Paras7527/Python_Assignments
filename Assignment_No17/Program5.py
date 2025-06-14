#Schedule a job that runs every 5 minuites to write the current time to file Marvellous.txt
import time
import datetime
import schedule

def Scheduling():
    print("The Current Date & Time is : ",datetime.datetime.now())

    fobj=open("Marvellous.txt","a")
    fobj.write(str(datetime.datetime.now())+"\n")

def main():
    print("Inside the Automation Application : ")

    print("The current time is : ",datetime.datetime.now())

    schedule.every(5).minute.do(Scheduling)

    print("Application is in running state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()