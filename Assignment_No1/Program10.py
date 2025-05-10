#Write a program which accept name for user and display length of its name.
import sys

def main():
    print("Enter the String : ")
    str=input()
    
    #print(sys.getsizeof(str))  Get the Actual size of string.
    print("The length of string is : ",len(str))
    
if __name__=="__main__":
    main()