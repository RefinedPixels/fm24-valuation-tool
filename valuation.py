import pandas as pd
from position_weights import POSITION_WEIGHTS

# Load data
df = pd.read_csv("../data/players_sample.csv")

# Position Score calculation
def calculate_position_score(row):
    weights = POSITION_WEIGHTS.get(row["Position"], {})
    if not weights:
        return 0
    total = sum(row.get(attr, 0) * weight for attr, weight in weights.items())
    return total / sum(weights.values())

df["Position Score"] = df.apply(calculate_position_score, axis=1)

# PA Score
df["PA Score"] = (df["PA"] / 200) * 100

# Development Score
df["Development Score"] = ((100 - df["Age"]) * (df["PA"] - df["CA"])) / 100

# True Value Score
df["True Value Score"] = (
    df["Position Score"] * 0.5 +
    df["PA Score"] * 0.3 +
    df["Development Score"] * 0.2
)

# Bargain Detector
df["Buy Rating"] = df.apply(
    lambda row: "BUY" if row["True Value Score"] > (row["Market Value"] / 100000) else "",
    axis=1
)

# Save result
df.to_csv("../data/players_valued.csv", index=False)
print("Valuation complete. Check data/players_valued.csv")
