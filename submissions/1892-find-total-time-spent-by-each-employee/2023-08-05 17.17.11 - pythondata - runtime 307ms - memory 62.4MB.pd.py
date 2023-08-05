import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees[['event_day', 'emp_id', 'total_time']]
    employees = employees.groupby(['emp_id', 'event_day'], as_index=False).sum()
    employees.rename({'event_day': 'day'}, axis=1, inplace=True)
    return employees