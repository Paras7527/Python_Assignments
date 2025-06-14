#write a script to remove all blank lines from a file.save the cleaned output to new line

def main():
    fobj=open("Program5.txt","r")

    lines=fobj.readlines()

    fobj.close()
    
    clean_lines=[]
    for line in lines:
        if line.strip() != "":
            clean_lines.append(line)

    fobj2 = open("Cleaned.txt", "w")

    for line in clean_lines:
        fobj2.write(line)

    fobj2.close()
    
if __name__=="__main__":
    main()