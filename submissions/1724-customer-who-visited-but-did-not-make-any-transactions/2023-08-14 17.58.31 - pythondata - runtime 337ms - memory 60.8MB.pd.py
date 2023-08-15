import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return visits[~visits['visit_id'].isin(transactions['visit_id'].unique())].groupby(by='customer_id', as_index=False).count().rename({'visit_id': "count_no_trans"}, axis=1)