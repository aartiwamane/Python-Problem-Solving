
def ReverseDigit(Value):
    Reverse = 0
    Digit = 0
   

    while(Value != 0):
        Digit = (Value%10)
        Value = Value//10
        Reverse = (Reverse *10)+Digit
        

    return Reverse

def main():
    Digit = int(input("Enter a digit Value : "))

    Ret = ReverseDigit(Digit)
    print("Reverse of the digit is :",Ret)

if __name__ == "__main__":
    main()