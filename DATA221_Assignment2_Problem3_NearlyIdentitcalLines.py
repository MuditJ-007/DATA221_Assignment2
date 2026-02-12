#Mudit Jindal
#Problem 3 - Almost Identical Lines

import string

normalized = {}
duplicate_sets = []

with open("sample-file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    cleaned = line.lower()
    cleaned = cleaned.replace(" ", "").replace("\n", "")
    cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))

    if cleaned in normalized:
        normalized[cleaned].append((i+1, line.strip()))
    else:
        normalized[cleaned] = [(i+1, line.strip())]

for group in normalized.values():
    if len(group) > 1:
        duplicate_sets.append(group)

print("Number of duplicate sets:", len(duplicate_sets))

print("\nFirst two sets:")
for group in duplicate_sets[:2]:
    for num, text in group:
        print(f"{num}: {text}")
    print()
