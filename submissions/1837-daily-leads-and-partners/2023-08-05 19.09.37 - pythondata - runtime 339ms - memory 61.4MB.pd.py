import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name'], as_index=False).nunique().rename({'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, axis=1)