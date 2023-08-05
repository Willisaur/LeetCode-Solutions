import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    employees["bonus"] = employees["bonus"].where((employees["name"].str[0] == "M") | (employees["employee_id"] % 2 == 0), employees["salary"], axis = 0)

    return employees[["employee_id", "bonus"]].sort_values("employee_id")
