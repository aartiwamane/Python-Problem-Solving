def CalculateOdd(Value):
    return (Value%2 != 0)

def main():
    Data = [12,4,20,25,30,67,51]

    FData = list(filter(CalculateOdd,Data))
    print(" Odd Elements from List : ",FData)

if __name__ == "__main__":
    main()