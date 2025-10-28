#3)Input a sentence or a paragraph from user and extract how many unique words are used and display the count

text = input("Enter a sentence or paragraph:").lower()

import string
text= text.translate(str.maketrans('', '', string.punctuation))
words = text.split()
unique_words = set(words)
unique_words_count = len(unique_words)
print("Number of unique words:", unique_words_count)