#Mudit Jindal
#Problem10: Reusable Search Function

def find_lines_containing(filename, keyword):
    results = []

    with open(filename, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                results.append((i, line.strip()))

    return results


matches = find_lines_containing("sample-file.txt", "lorem")

print("Total matches:", len(matches))

for line in matches[:3]:
    print(line)
