def PrimeCalculate(No):
    
    if (No <= 1):
        return False
    
    for i in range(2,No):
        if(No%i == 0):
           return False
    
    return True
   
def main():

    Value1 = int(input("Enter First number : "))
    
    Ret = PrimeCalculate(Value1)

    if Ret:
        print(f"{Value1} Number is Prime Number ")

    else:
        print(f"{Value1} Number is not a Prime Number ")
    
if __name__ =="__main__":
    main()