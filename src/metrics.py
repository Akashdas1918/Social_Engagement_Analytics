
import numpy as np
import pandas as pd

def add_engagement_metrics(df):
    x = df.copy()
    denom = x["reach"].replace(0, np.nan)
    x["engagements"] = x[["likes","comments","shares","saves"]].sum(axis=1)
    x["engagement_rate"] = (x["engagements"] / denom * 100).fillna(0)
    x["share_rate"] = (x["shares"] / denom * 100).fillna(0)
    x["save_rate"] = (x["saves"] / denom * 100).fillna(0)
    x["save_to_share_ratio"] = x["saves"] / x["shares"].replace(0, np.nan)
    # Viral coefficient proxy: high-value actions weighted more than likes.
    x["viral_coefficient"] = ((2*x["shares"] + 2*x["saves"] + x["comments"]) / denom).fillna(0)
    threshold = x["viral_coefficient"].quantile(.80)
    x["high_viral_potential"] = (x["viral_coefficient"] >= threshold).astype(int)
    return x, float(threshold)
