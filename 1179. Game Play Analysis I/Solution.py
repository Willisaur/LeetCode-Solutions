import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby(["player_id"], as_index=False)["event_date"].min()
    activity.rename({"event_date": "first_login"}, axis=1, inplace=True)
    
    return activity