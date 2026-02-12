#Mudit Jindal
#Problem 4: DATA221_Assignment2_Problem4_DataFilteration

import pandas as pd
df = pd.read_csv("student.csv")

filtered = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

filtered.to_csv("high_engagement.csv", index=False)

print("Students saved:", len(filtered))
print("Average grade:", filtered["grade"].mean())
