import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    temp = courses.groupby('class').count()
    return temp[temp['student'] >=5].reset_index()[['class']]