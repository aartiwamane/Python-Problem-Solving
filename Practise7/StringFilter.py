def LargeString(Value):
    
    if (len(Value)>5):
        return Value

def main():
    Data = ["Aarti","Amit","Ashutosh","Nitashri","Sita"]

    FData = list(filter(LargeString,Data))
    print(" String having more than 5 characters : ",FData)

if __name__ == "__main__":
    main()