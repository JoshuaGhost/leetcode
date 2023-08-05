import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    counts = pd.cut(
        accounts.income,
        [-float('inf'), 19999, 50000, float('inf')],
        right=True,
        labels=['Low Salary', 'Average Salary', 'High Salary']
    ).value_counts()
    return pd.DataFrame({'category': counts.index, 'accounts_count': counts.values})
                                    