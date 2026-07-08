def CalculateDigit(No):
    Digit = 0
    Count = 0
    while(No != 0):
        Count=Count+1
        No = No//10
    return Count
   
def main():

    Value1 = int(input("Enter a number : "))
    
    Ret = CalculateDigit(Value1)
    print(f"Total Digits from Number are {Ret}")
    
if __name__ =="__main__":
    main()