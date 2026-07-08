def Display(No):
    
    for i in range(No):
        for j in range(No):
            print("*",end="")
        print()
   
def main():

    Value1 = int(input("Enter First number : "))
    
    Display(Value1)
    
if __name__ =="__main__":
    main()