import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    temp = examinations.groupby(['student_id', 'subject_name'], as_index=False).agg(attended_exams=('subject_name', 'count'))
    students = students.merge(subjects, how='cross')
    students = students.merge(temp, how='left', on=['student_id', 'subject_name']).fillna(0)
    return students.sort_values(['student_id', 'subject_name'])[['student_id', 'student_name', 'subject_name', 'attended_exams']]