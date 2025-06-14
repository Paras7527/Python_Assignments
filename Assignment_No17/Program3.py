#Write a program that schedules a function to print "do coding" every 30 minuites
import time
import datetime
import schedule

def Scheduling():
    print("Do Coding...!")

def main():
    print("The Current time is : ",datetime.datetime.now())

    schedule.every(30).minute.do(Scheduling)

    print("Application is in Waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=="__main__":
    main()