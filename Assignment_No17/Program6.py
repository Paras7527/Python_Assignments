#Write a script that schedules multiple tasks : one to print "Lunch time!" at 1p.m and another to print "Wrap up work!" at 6 p.m

import time 
import datetime
import schedule

def Scheduling1():
    print("Its Lunch Time!🍽️")

def Scheduling2():
    print("Wrap up work!🍽️")

def main():
    print("Inside the Automation Application")

    print("The Current Time is : ",datetime.datetime.now())

    schedule.every().day.at("13:00").do(Scheduling1)

    schedule.every().day.at("18:00").do(Scheduling2)

    print("The Automation Application is in Running State..... ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()