#2) Get input from user and check if it is palindrome

word = input("Enter word:").lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("The words are palindrome")
else:
  print("The words are not palindrome")