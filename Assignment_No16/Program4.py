#Accept 10 numbers from user and write them into file named as number.txt, each on new line 
def main():
    fobj=open("number.txt","w")

    print("Enter the numbers that you want to store in file :")   
    Value=int(input()) 

    print("Enter the Elements")
    for i in range(1,Value+1):
        no=int(input())
        fobj.write(str(no)+"\n")
    
        
if __name__=="__main__":
    main()