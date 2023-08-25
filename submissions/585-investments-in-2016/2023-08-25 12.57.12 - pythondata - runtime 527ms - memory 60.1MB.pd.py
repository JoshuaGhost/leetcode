import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['nd_tiv_2015'] = insurance.groupby('tiv_2015')['pid'].transform('count')
    insurance['nd_lat_lon'] = insurance.groupby(['lat', 'lon'])['pid'].transform('count')
    s = round(insurance[(insurance['nd_tiv_2015'] != 1) & (insurance['nd_lat_lon'] == 1)]['tiv_2016'].sum(), 2)
    return pd.DataFrame({'tiv_2016': [s]})
