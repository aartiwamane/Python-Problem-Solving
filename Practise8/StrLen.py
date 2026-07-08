def StringLenth(Data):
    count = 0
    for i in Data:
        count = count+1
    return count
   
def main():

    String = (input("Enter a String : "))
    
    Ret = StringLenth(String)
    print(f"Length of given string is : {Ret}")
    
if __name__ =="__main__":
    main()