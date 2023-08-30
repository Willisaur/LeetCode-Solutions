import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    collab_counts = actor_director.groupby(["actor_id", "director_id"], as_index=False).nunique()
    actor_director = collab_counts[collab_counts["timestamp"] > 2]

    return actor_director[["actor_id", "director_id"]]