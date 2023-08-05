import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[['teacher_id', 'subject_id']].drop_duplicates().groupby(by='teacher_id', as_index=False).count().rename({'subject_id': 'cnt'}, axis=1)