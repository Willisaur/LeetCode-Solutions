import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # rename columns
    # merge departments onto employee df & drop department ID
    # filter to only the highest salaries for each department 
    
    employee.columns = ["eId", "Employee", "Salary", "id"]
    employee = employee.merge(department, on="id", how="left")
    employee = employee[["Employee", "Salary", "name"]].rename({"name": "Department"}, axis=1)

    answers = pd.DataFrame([], columns = employee.columns)

    for department in employee["Department"].unique():
        df_dept = employee[employee["Department"] == department]
        
        df_dept = df_dept[df_dept["Salary"] == df_dept["Salary"].max()]
        
        answers = answers.merge(df_dept, how="outer")

    return answers[["Department", "Employee", "Salary"]]
   