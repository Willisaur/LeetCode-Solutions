import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # drop the duplicate salaries (tied rankings mess up result)
    salaries = employee["salary"].drop_duplicates()
    salaries = salaries.sort_values(ascending=False)

    second = 0
    if salaries.shape[0] < 2:
        second = None
    else:
        second = salaries.iloc[1]
    
    return pd.DataFrame([second], columns=["SecondHighestSalary"])