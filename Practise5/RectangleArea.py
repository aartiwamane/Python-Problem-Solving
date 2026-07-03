def Area(Value1,Value2):
     return Value1*Value2

def main():
    No1 = int(input("Enter the Length of Rectangle : "))
    No2 = int(input("Enter the Width of Rectangle : "))

    Ret = Area(No1, No2)
    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()