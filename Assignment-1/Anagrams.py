# 1) Take input from user for two words, and check if they are anagrams (anagram example: listen and silent -> both contain the same number and set of alphabets)

wordOne = input("Enter first word:").lower()
wordTwo = input("Enter second word:").lower()
if sorted(wordOne) == sorted(wordTwo):
    print("The words are anagrams")
else:
    print("The words are not anagrams")