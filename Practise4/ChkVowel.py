def ChkVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        return True
    else:
        return False

def main():
    char = input("Enter the Character : ")

    Ret = ChkVowel(char)
    
    if(Ret == True):
        print("Character is Vowel..")
    else:
        print("Character is consonants..")

if __name__ == "__main__":
    main()