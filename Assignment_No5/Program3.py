#Voting Eligibility Checker
from Functions import CheckVoteEligibility

def main():
    print("Enter the Age : ")
    iValue=int(input())

    iRet=CheckVoteEligibility(iValue)
    if(iRet==True):
        print("Person is Eligible to Vote.")
    else:
        print("Person is Not Eligible.")

if __name__ == "__main__":
    main()