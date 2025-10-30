
#2. Accept a word/sentence from the user and count how many vowels (a, e, i, o, u) are present in it.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    text= text.lower()
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

input_text = input("Enter the text to be counted ")
print("Number of vowels:",count_vowels(input_text))