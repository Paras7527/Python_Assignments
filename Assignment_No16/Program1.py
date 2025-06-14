#Write a program which creates a text file named as student.txt write a names of 5 student into it
def main():
    print("Enter the name of File : ")
    FileName=input()

    fobj=open(FileName,"w")

    fobj.write("Paras Kulkarni\n")
    fobj.write("Manasi Kulkarni\n")
    fobj.write("Ayush Kulkarni\n")
    fobj.write("Abhishek Kulkarni\n")
    fobj.write("Vaibhav Kulkarni\n")

    fobj.close()
    
if __name__=="__main__":
    main()