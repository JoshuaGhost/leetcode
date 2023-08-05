import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    temp = employee.merge(department, left_on=['departmentId'], right_on=['id'], suffixes=('_e', '_d'))
    temp = temp.groupby('departmentId', sort=True).apply(lambda x: x[x.salary == x.salary.max()])
    return temp[['name_d', 'name_e', 'salary']].rename({
        'name_d': "Department", 
        'name_e': "Employee",
        "salary_e": "Salary"},
        axis=1
    )