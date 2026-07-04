# [on_true] if [expression] else [on_false]

# x, y = 50, 25
# small = x if x < y else y

FindMax = lambda Value1,Value2,Value3 : Value1 if (Value1>Value2 and Value1>Value3) else Value2 if (Value2 > Value1 and Value2 > Value3) else Value3
        
def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))
    No3 = int(input("Enter Third Number : "))

    Ret = FindMax(No1,No2,No3)

    print("This is Maximum Number : ",Ret)


if __name__ == "__main__":
    main()