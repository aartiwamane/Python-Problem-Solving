def FactCalculate(Value):
    Factors = list()

    for i in range (1,Value+1):
        if(Value % i == 0):
            Factors.append(i)
    return Factors

def main():
    No = int(input("Enter the number to calculate factos : "))

    Ret = FactCalculate(No)
    print("Factors of the number are : ",Ret)

if __name__ == "__main__":
    main()