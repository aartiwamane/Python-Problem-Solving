from  functools import reduce

def Addition(Value1, Value2):
    return Value1+Value2

def main():
    Data = [12,4,20,25,30]

    RData = reduce(Addition,Data)
    print("Elements Addition: ",RData)

if __name__ == "__main__":
    main()