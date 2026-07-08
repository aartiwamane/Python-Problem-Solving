
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5


def Display(No):
    
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(i,end="\t")
        print()
   
def main():

    Value1 = int(input("Enter a Number : "))
    
    Display(Value1)
    
if __name__ =="__main__":
    main()