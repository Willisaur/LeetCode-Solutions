import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"], as_index=False)["total_time"].sum()
    employees = employees.rename({"event_day": "day"}, axis=1)

    return employees