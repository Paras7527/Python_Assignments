#Create a task that run once every day at 9.00 A.M and prints "NAMASKAR 🙏🏻"
import time
import datetime
import schedule

def Scheduling():
    print("Namaskar...!🙏🏻",datetime.datetime.now())

def main():
    print("Inside Automation Application : ")

    schedule.every().day.at("09:00").do(Scheduling)

    print("Application is in Running state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()