import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    temp = employee[~employee.managerId.isna()].groupby('managerId', as_index=False).count()
    temp = temp[temp['name'] >= 5][['managerId', 'id']]
    return temp.merge(employee, left_on='managerId', right_on='id')[['name']]