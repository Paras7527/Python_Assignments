#Write a program to copy contents of one file into another file.
import sys
def main():
    fobj=sys.argv[1]

    Demo1=open(fobj,"r")

    Demo2=open("Demo2.txt","w")

    Demo2.write(Demo1.read())

if __name__=="__main__":
    main()