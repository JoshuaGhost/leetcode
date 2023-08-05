import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    temp = (
    employee[['salary']]
        .sort_values('salary', ascending=False)
        .drop_duplicates(subset=['salary'])
        .rename({"salary": "SecondHighestSalary"}, axis=1)
    )
    if len(temp) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    return temp.iloc[1:2]