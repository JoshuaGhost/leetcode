import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    res = len(delivery[delivery['customer_pref_delivery_date'] == delivery['order_date']])/len(delivery)
    res = round(res * 100, 2)
    return pd.DataFrame({'immediate_percentage': [res]})