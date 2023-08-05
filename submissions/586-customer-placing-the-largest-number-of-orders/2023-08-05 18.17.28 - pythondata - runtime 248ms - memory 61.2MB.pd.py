import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_count = orders.groupby('customer_number').count()
    max_order_count = order_count.max().values[0]
    return order_count[order_count['order_number'] == max_order_count].reset_index()[['customer_number']]
