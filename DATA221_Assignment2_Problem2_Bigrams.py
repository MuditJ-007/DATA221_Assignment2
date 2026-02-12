#Mudit Jindal
#Data221 Problem 2- Bigrams

import string
from collections import Counter

# Read file
with open("sample-file.txt", "r", encoding="utf-8") as file:
    text = file.read()

tokens = text.split()

clean_tokens = []

for word in tokens:
    word = word.lower()
    word = word.strip(string.punctuation)

    letters = sum(c.isalpha() for c in word)

    if letters >= 2:
        clean_tokens.append(word)

# Create bigrams
bigrams = []

for i in range(len(clean_tokens) - 1):
    pair = clean_tokens[i] + " " + clean_tokens[i+1]
    bigrams.append(pair)

# Count
counts = Counter(bigrams)

for pair, count in counts.most_common(5):
    print(f"{pair} -> {count}")
