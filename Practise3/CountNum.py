
def CountDigit(Value):
    Count = 0

    while(Value != 0):
        Value = Value//10
        Count = Count+1

    return Count

def main():
    Digit = int(input("Enter a digit Value : "))

    Ret = CountDigit(Digit)
    print("Count of numbers in digit is :",Ret)

if __name__ == "__main__":
    main()