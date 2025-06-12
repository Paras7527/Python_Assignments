#write a program which accept the file name from user and create new file named and Demo.txt and copy all the contents from existing file into new file .Accept file through command line args
import sys

def main():
    fobj=sys.argv[1]

    Demo1=open(fobj,"r")

    Demo2=open("Demo2.txt","w")

    Demo2.write(Demo1.read())

if __name__=="__main__":
    main()