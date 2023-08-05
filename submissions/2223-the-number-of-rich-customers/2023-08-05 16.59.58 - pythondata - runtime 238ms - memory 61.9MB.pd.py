import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    group_res = store.groupby(by='customer_id').max()
    return pd.DataFrame({'rich_count': [len(group_res[group_res['amount'] > 500])]})