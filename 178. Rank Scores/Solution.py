import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores[["score"]].sort_values("score", ascending=False)
    scores["rank"] = scores.rank(method="dense", ascending=False)

    return scores