#Mudit Jindal
#DATA 221 - Problem 1 - Reading a File

import string
from collections import Counter

# Step 1: Read the file
with open("sample-file.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 2: Split into words (tokens)
words_in_my_file = text.split()

# Step 3-5: Clean each token
my_cleaned_tokens = []
for my_words in words_in_my_file:
    # Convert to lowercase
    my_words = my_words.lower()

    # Remove punctuation from beginning and end
    my_words = my_words.strip(string.punctuation)

    # Keep only the words with at least 2 alphabetic characters
    my_letters = sum(character.isalpha() for character in my_words)
    if my_letters >=2:
        my_cleaned_tokens.append(my_words)

# Step 6: Count word frequencies
# Counter is a special dictionary that counts items
word_counts = Counter(my_cleaned_tokens)

# Step 7: Get the 10 most common words and print in the requested format

for word, count in word_counts.most_common(10):
    print(f"{words_in_my_file} - {count}")
