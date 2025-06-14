#create a file marks.txt with student name and marks .then read the file and display the student who scored nore than 75 marks

def main():
    fobj=open("marks.txt","w")

    print("Enter the Number :")
    iValue=int(input())

    fobj.write("Name"+"\t"+"Marks"+"\n")
    for i in range(1,iValue+1):
        no=input("Name of the Student :")
        no1=int(input("Marks of Student :"))
        fobj.write(f"{no}\t{no1}\n")

    fobj.close()

    fobj=open("marks.txt","r")
    lines=fobj.readlines()
    fobj.close()

    for i in lines[1:]:
        parts=i.strip().split("\t")
        name=parts[0]
        marks=parts[1]

        if (int(marks) > 75):
            print(f"{name}->{marks}")

if __name__=="__main__":
    main()