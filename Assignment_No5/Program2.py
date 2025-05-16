#Accept single char from user and check whether it is vowel if not print its consonants
from Functions import CheckVowels

def main():
    print("Enter the CHaracter : ")
    str=input()

    iRet=CheckVowels(str)
    if(iRet==True):
        print("The Character is a Vowel")
    else:
        print("The Character is Consonant")

if __name__ == "__main__":
    main()