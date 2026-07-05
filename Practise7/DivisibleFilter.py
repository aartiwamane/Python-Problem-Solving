def DivisibleThreeFive(Value):
    return (Value%3 == 0 and Value%5 == 0)

def main():
    Data = [12,15,20,25,30,67,60]

    FData = list(filter(DivisibleThreeFive,Data))
    print(" elements are divisible by 5 and 3 : ",FData)

if __name__ == "__main__":
    main()