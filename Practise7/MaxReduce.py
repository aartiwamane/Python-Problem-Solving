from  functools import reduce

def CalculateMax(Value1, Value2):
    if Value1>Value2:
        return Value1
    else:
        return Value2
def main():
    Data = [12,4,20,45,30]

    RData = reduce(CalculateMax,Data)

    print("Largest Element from list ",RData)

if __name__ == "__main__":
    main()