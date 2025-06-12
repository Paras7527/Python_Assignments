#Write a progra which accept two file names from user and compare the contents of both files .if both files contains the same content then display success otherwise failure.Accept both files from command line arguments.
import sys
def main():
    fobj1=sys.argv[1]
    fobj2=sys.argv[2]

    fobj1=open(fobj1,"r")
    fobj2=open(fobj2,"r")

    fobj1=fobj1.read()
    fobj2=fobj2.read()

    if(fobj1==fobj2):
        print("Success")
    else:
        print("Failure")

if __name__=="__main__":
    main()