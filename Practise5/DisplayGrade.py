 
def main():
    No = int(input("Enter the Marks to Display Grade : "))

    if(No >= 75):
        print("Distinction")
    elif(No >= 60):
        print("First Class")
    elif(No >= 50):
        print("Second Class")
    else:
        print("Fail")
    
if __name__ == "__main__":
    main()