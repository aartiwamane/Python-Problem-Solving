def CalculateSum(Data):
    Sum = 0
    for  i in range((Data+1)):
        Sum =Sum+i
    return Sum
    
def main():
    Value = int(input("Enter the number : "))

    Ret = CalculateSum(Value)
    print(Ret)
if __name__ == "__main__":
    main()