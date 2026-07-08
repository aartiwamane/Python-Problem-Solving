
CalculateMultiply = lambda Value1, Value2 : Value1*Value2

def main():
    No1 = int(input("Enter the First Number : "))
    No2 = int(input("Enter the First Number : "))

    Ret = CalculateMultiply(No1,No2)

    print(f"Multiplication of {No1} and {No2} is {Ret}")

if __name__ == "__main__":
    main()