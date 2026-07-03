
def SumDigit(Value):
  
    Digit = 0
    Sum = 0

    while(Value != 0):
        Digit = Value%10
        Value = Value//10
        Sum = Sum+Digit

    return Sum

def main():
    Digit = int(input("Enter a digit Value : "))

    Ret = SumDigit(Digit)
    print("Sum of numbers in digit is :",Ret)

if __name__ == "__main__":
    main()