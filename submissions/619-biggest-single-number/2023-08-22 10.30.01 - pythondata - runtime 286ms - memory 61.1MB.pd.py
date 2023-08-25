import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers['count'] = my_numbers.groupby('num', as_index=False)['num'].transform('count')
    return pd.DataFrame({'num': [my_numbers[my_numbers['count'] == 1]['num'].max()]})