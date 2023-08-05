import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[['teacher_id', 'subject_id']].groupby(by='teacher_id', as_index=False).nunique().rename({'subject_id': 'cnt'}, axis=1)