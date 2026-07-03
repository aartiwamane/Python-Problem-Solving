def Area(Value1):
     return 3.14*Value1*Value1

def main():
    No1 = int(input("Enter the Radius of Circle : "))
    

    Ret = Area(No1)
    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()