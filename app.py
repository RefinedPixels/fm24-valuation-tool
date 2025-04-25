import streamlit as st
import pandas as pd
from scripts.position_weights import POSITION_WEIGHTS

st.title("⚽ FM24 Player Valuation Tool")

uploaded_file = st.file_uploader("Upload your player CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    def calculate_position_score(row):
        weights = POSITION_WEIGHTS.get(row["Position"], {})
        if not weights:
            return 0
        total = sum(row.get(attr, 0) * weight for attr, weight in weights.items())
        return total / sum(weights.values()) if weights else 0

    df["Position Score"] = df.apply(calculate_position_score, axis=1)
    df["PA Score"] = (df["PA"] / 200) * 100
    df["Development Score"] = ((100 - df["Age"]) * (df["PA"] - df["CA"])) / 100
    df["True Value Score"] = (
        df["Position Score"] * 0.5 +
        df["PA Score"] * 0.3 +
        df["Development Score"] * 0.2
    )
    df["Buy Rating"] = df.apply(
        lambda row: "BUY" if row["True Value Score"] > (row["Market Value"] / 100000) else "",
        axis=1
    )

    st.success("Valuation complete!")
    st.dataframe(df.sort_values("True Value Score", ascending=False))

    st.download_button("Download CSV", df.to_csv(index=False), "valued_players.csv", "text/csv")
