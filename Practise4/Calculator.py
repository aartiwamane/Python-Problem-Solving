def Addition(Value1,Value2):
     return Value1+Value2

def Substraction(Value1,Value2):
     return Value1-Value2

def Multiplication(Value1,Value2):
     return Value1*Value2

def Division(Value1,Value2):
     return Value1/Value2

def main():
    No1 = int(input("Enter the first Number : "))
    No2 = int(input("Enter the second Number : "))

    Ret = Addition(No1, No2)
    print("Addition of the number is : ",Ret)

    Ret1 = Substraction(No1, No2)
    print("Addition of the number is : ",Ret1)

    Ret2 = Multiplication(No1, No2)
    print("Addition of the number is : ",Ret2)

    Ret3 = Division(No1, No2)
    print("Addition of the number is : ",Ret3)

if __name__ == "__main__":
    main()