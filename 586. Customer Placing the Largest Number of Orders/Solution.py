import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    orders_counts = orders.groupby("customer_number", as_index=False)["order_number"].count()
    customer_max = orders_counts[orders_counts["order_number"] == orders_counts["order_number"].max()]["customer_number"]

    return pd.DataFrame({"customer_number": customer_max})