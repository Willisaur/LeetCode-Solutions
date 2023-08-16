import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    #if orders.shape[0] == 0:
    #    return orders.drop("order_number", axis=1)

    orders_counts = orders.groupby("customer_number", as_index=False)["order_number"].count()
    orders_max = orders_counts["order_number"].max()
    customer_max = orders_counts[orders_counts["order_number"] == orders_max]["customer_number"]

    return pd.DataFrame({"customer_number": customer_max})