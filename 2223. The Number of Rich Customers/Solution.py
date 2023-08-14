import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    highest = store.groupby("customer_id", as_index=False).max()
    count = len(highest[highest["amount"] > 500])
    return pd.DataFrame([count], columns = ["rich_count"])