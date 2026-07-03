def FactCalculate(Value):
    Sum = 0
    for i in range (1,Value):
        if(Value % i == 0):
            Sum = Sum+i
    return Sum

def ChkPerfect(Value):
    Res = 0
    Res = FactCalculate(Value)

    return (Res == Value)
    
def main():
    No = int(input("Enter the number to check perfect number : "))

    Ret = ChkPerfect(No)
    if(Ret == True):
        print("Number is Perfect Number..")
    else:
        print("Number is not perfect number..")

    
if __name__ == "__main__":
    main()