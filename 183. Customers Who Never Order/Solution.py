import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    noOrders = customers[~customers["id"].isin(orders["customerId"])]
    noOrders = noOrders[["name"]]
    noOrders.columns = ["Customers"]
    return noOrders
