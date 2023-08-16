import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby("class", as_index=False)["student"].nunique()
    courses = courses[courses["student"] > 4]
    courses = courses.drop("student", axis=1)
    return courses