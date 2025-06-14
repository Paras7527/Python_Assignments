#Schedule a task that displays the current date and time every minuite using the date time method
import time
import datetime
import schedule

def Scheduling():
    print("The Current Date & Time is : ",datetime.datetime.now())

def main():
    print("Inside the Automation application : ")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minute.do(Scheduling)

    print("Application is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()