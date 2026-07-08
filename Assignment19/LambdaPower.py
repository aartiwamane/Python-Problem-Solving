
CalculatePower = lambda Value: Value**2

def main():
    No = int(input("Enter the Number : "))

    Ret = CalculatePower(No)
    print(f"Power 2 of a {No} is {Ret}")

if __name__ == "__main__":
    main()