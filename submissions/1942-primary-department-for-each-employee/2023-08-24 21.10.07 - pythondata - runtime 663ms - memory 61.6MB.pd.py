import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['dep_cnt'] = employee.groupby('employee_id')['department_id'].transform('nunique')
    return employee[
        (employee['primary_flag'] == 'Y') 
        | (employee['dep_cnt'] == 1)
    ][['employee_id', 'department_id']]