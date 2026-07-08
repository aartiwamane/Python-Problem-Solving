def FactCalculateSum(No):
    
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum+i
    return Sum
   
def main():

    Value1 = int(input("Enter First number : "))
    
    Ret = FactCalculateSum(Value1)
    print(f"Addition of Factors of a number is {Ret}")
    
if __name__ =="__main__":
    main()