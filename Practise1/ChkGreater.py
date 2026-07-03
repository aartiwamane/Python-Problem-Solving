def ChkGreater(Value1,Value2):
    if(Value1>Value2):
        return Value1
    else:
        return Value2



def main():
    No1 = int(input("Enter First number :"))
    No2 = int(input("Enter Second number :"))

    Solution = ChkGreater(No1,No2)
    print(Solution,"is Greater number")

if __name__ == "__main__":
    main()