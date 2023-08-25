import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    uniq_pos = insurance.drop_duplicates(['lat', 'lon'], keep=False).pid
    duplicated_2015 = insurance[insurance.duplicated('tiv_2015', keep=False)].pid
    return insurance[insurance.pid.isin(uniq_pos) & insurance.pid.isin(duplicated_2015)][['tiv_2016']].sum().to_frame('tiv_2016').round(2)
