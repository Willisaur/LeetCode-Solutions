import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(["date_id", "make_name"], as_index=False).nunique()
    daily_sales.rename({"lead_id":"unique_leads", "partner_id": "unique_partners"}, axis=1, inplace=True)
    return daily_sales