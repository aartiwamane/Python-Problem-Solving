def DivisibleBy(Value1):
    if((Value1%3 == 0) and (Value1%5 == 0)):
        return True
    else:
        return False
    
def main():
    No1 = int(input("Enter First number :"))

    Solution = DivisibleBy(No1)

    if(Solution == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

    
if __name__ == "__main__":
    main()