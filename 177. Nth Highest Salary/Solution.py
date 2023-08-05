import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    no_dups = employee["salary"].drop_duplicates()

    sorted_salaries = no_dups.sort_values(ascending=False)
    nthSalary = 0

    if sorted_salaries.shape[0] < N:
        nthSalary = None
    else:
        nthSalary = sorted_salaries.iloc[N-1]
    
    return pd.DataFrame([nthSalary], columns=[f"getNthHighestSalary{N})"])