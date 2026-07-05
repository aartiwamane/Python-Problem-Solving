from  functools import reduce

def Multiplication(Value1, Value2):
    return Value1*Value2

def main():
    Data = [12,4,20,25]

    RData = reduce(Multiplication,Data)
    print("Elements Multiplication: ",RData)

if __name__ == "__main__":
    main()