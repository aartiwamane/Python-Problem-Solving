def CalculateEven(Value):
    return (Value%2 == 0)

def main():
    Data = [12,4,20,25,30,67]

    FData = list(filter(CalculateEven,Data))
    print(" Even Elements from List : ",FData)

if __name__ == "__main__":
    main()