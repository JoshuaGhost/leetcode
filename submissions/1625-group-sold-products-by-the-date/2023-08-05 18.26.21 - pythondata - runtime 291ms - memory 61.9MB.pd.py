import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date', as_index=False)['product'].agg([
        ('num_sold', 'nunique'),
         ('products', lambda x: ','.join(sorted(x.unique())))])