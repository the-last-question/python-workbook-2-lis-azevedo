def palindrome(word):
    return word == word[::-1]

def main():
    word = input("Input: ")
    print(word + " is a palindrome") if(palindrome(word)) else print(word + " is not a palindrome")
        
if __name__ == "__main__": main()