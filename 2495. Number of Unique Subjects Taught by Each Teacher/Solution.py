import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby("teacher_id", as_index=False)["subject_id"].nunique()
    teacher.rename({"subject_id":"cnt"}, axis=1, inplace=True)
    return teacher