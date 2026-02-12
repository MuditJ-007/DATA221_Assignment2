#Mudir Jindal
#Problem 5: Summary Tables

import pandas as pd
df = pd.read_csv("student.csv")

def get_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(get_band)

summary = df.groupby("grade_band").agg(
    number_of_students=("grade", "count"),
    average_absences=("absences", "mean"),
    percent_with_internet=("internet", "mean")
)

summary["percent_with_internet"] *= 100

summary.to_csv("student_bands.csv")

print(summary)


