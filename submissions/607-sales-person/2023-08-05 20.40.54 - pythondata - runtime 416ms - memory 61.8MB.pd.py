import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    temp = company[company.name.str.match('RED')][['com_id']]
    temp = temp.merge(orders, on='com_id')
    temp = temp.merge(sales_person, on='sales_id')['name']
    return sales_person[~sales_person.name.isin(temp)][['name']]