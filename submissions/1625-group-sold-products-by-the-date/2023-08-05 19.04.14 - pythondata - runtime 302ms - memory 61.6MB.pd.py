import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    temp = activities.groupby('sell_date', as_index=False).agg([('num_sold','nunique'), ('products', lambda x: ','.join(sorted(x.unique())))])
    temp.columns = [
        '_'.join(col).rstrip('_') for col in temp.columns.values
    ]
    return temp.rename({'product_num_sold': 'num_sold', 'product_products': 'products'}, axis=1).reset_index()