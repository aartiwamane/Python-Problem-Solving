
def CountDigit(Value):
    Sum = 0
    Digit = 0

    while(Value != 0):
        Digit = Value%10
        Value = Value//10
        Sum = Sum+Digit

    return Sum

def main():
    Digit = int(input("Enter a digit Value : "))

    Ret = CountDigit(Digit)
    print("Addition of Digits in Number is :",Ret)

if __name__ == "__main__":
    main()