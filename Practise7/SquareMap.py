def CalculateSquare(Value):
    return Value*Value

def main():
    Data = [12,4,20,25,30]

    MData = list(map(CalculateSquare,Data))
    print("Elements Aftre Square : ",MData)

if __name__ == "__main__":
    main()