#Schedule a function that performs file backup every hour and writes a log entry in backup_log.txt

import time
import datetime
import schedule

def Scheduling():
    fobj=open("Backup_Log.txt","a")
    fobj.write(str(datetime.datetime.now())+"\n")
    fobj.close()


def main():
    print("Inside the Automation Application : ")

    schedule.every(1).hour.do(Scheduling)

    print("Application is in running state...")

    while True:
        schedule.run_pending()
        time.sleep(1)

    

if __name__=="__main__":
    main()