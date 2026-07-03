def CalculatePrime(No):
        
    if No<=1:
        return False
    
    i = 2
    while i<=No/2:
        if(No%i==0):
            return False
        i = i +1
    return True

def main():
    Value = int(input("Enter the number : "))

    Ret = CalculatePrime(Value)
    if(Ret == False):
        print("Number is not Prime number")
    else:
        print("Number is prime number")


if __name__ == "__main__":
    main()