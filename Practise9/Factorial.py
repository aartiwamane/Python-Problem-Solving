def FactCalculate(No):
    
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact*i
    return Fact
   
def main():

    Value1 = int(input("Enter First number : "))
    
    Ret = FactCalculate(Value1)
    print(f"Factorial of a number is {Ret}")
    
if __name__ =="__main__":
    main()