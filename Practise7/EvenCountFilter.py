def CalculateEven(Value):
    i = 0
    if (Value%2 == 0):
        i = i+1
    return i

def main():
    Data = [12,4,20,25,30,67,78]

    FData = list(filter(CalculateEven,Data))
    print(" Even Elements Counts from List : ",len(FData))

if __name__ == "__main__":
    main()