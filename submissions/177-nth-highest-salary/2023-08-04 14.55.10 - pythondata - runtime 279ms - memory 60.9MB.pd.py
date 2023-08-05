import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    return (
        employee[['salary']]
        .sort_values('salary', ascending=False)
        .drop_duplicates(subset=['salary'])
        .rename({"salary": f'getNthHighestSalary({N})'})
        .iloc[N-1:N]
    )