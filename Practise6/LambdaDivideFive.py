
ChkDivisible = lambda Value1:(Value1 % 5 == 0)
        
def main():
    No1 = int(input("Enter a Number :"))
    

    Ret = ChkDivisible(No1)
    if Ret:
        print("The Number is Divisible by 5..")
    else:
        print("The Number is not Divisible by 5...")

if __name__ == "__main__":
    main()