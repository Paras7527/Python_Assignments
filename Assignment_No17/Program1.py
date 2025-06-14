#Write a python script that prints "Jay Ganesh" every 2 seconds .Use the Secdule.every(2).do(...) function.
import sys
import datetime
import schedule
import time

def Scheduling():
    print("Jay Ganesh ...",datetime.datetime.now())

def main():
    print("Inside Automation Application : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(2).seconds.do(Scheduling)

    print("Application is in waiting state :")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()