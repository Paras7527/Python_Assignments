#Write a script that stimulates checking for email updates every 10 seconds(Use a print statement like "Checkin email" instead of real email logic)
import time
import schedule

def CheckEmail():
    print("Checking email...")

def main():
    print("Email Checking Simulation Started.")

    schedule.every(10).seconds.do(CheckEmail)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
