
def ReverseDigit(Value):
    Reverse = 0
    Digit = 0
   
    while(Value != 0):
        Digit = (Value%10)
        Reverse = (Reverse *10)+Digit
        Value = Value//10
        
    return Reverse

def ChkPalindrome(No):
    Rev = 0
    Rev = ReverseDigit(No)
    return (Rev == No)

def main():
    Digit = int(input("Enter a digit Value : "))

    Ret = ChkPalindrome(Digit)

    if (Ret == True):
        print("Number is Plindrome Number...")

    else:
        print("Number is not Palindrome number...")

if __name__ == "__main__":
    main()