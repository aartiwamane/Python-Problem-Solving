def Cube(Value1):
    return Value1*Value1*Value1



def main():
    No1 = int(input("Enter a number for calculating cube : "))
    Res = Cube(No1)
    print(Res)

if __name__ == "__main__":
    main()