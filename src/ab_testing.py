
import pandas as pd
from scipy.stats import mannwhitneyu
def compare_variants(df, metric="engagement_rate", group="content_format"):
    rows=[]
    for value in sorted(df[group].dropna().unique()):
        rows.append((value,df.loc[df[group]==value,metric].dropna().values))
    results=[]
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            a, av=rows[i]; b,bv=rows[j]
            if len(av) and len(bv):
                stat,p=mannwhitneyu(av,bv,alternative="two-sided")
                results.append({"variant_a":a,"variant_b":b,"median_a":float(pd.Series(av).median()),"median_b":float(pd.Series(bv).median()),"p_value":float(p)})
    return pd.DataFrame(results)
