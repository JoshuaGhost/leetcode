import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders['customer_number'].mode().to_frame()
    return orders