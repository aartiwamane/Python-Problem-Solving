def CalculateNums(Value):
    Series = list()

    for i in range (1,Value+1):
            Series.append(i)
    
    return Series

def main():
    No = int(input("Enter the number : "))

    Ret = CalculateNums(No)
    print("Series of the number are : ",Ret)

if __name__ == "__main__":
    main()