#Mudit Jindal
#Problem 6: Crime Levels vs Unemployment Levels

import pandas as pd

crime = pd.read_csv("crime.csv")

crime["risk"] = crime["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

result = crime.groupby("risk")["PctUnemployed"].mean()

for risk, avg in result.items():
    print(f"{risk} average unemployment: {avg}")
