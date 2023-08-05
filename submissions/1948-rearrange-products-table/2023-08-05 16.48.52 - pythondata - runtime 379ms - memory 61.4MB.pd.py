import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    final = []
    for i in range(1, 4):
        ret = pd.DataFrame()
        temp = products[['product_id', f'store{i}']]
        temp = temp[~temp[f'store{i}'].isnull()].reset_index()
        ret['product_id'] = temp['product_id']
        ret['store'] = pd.Series([f'store{i}'] * len(temp))
        ret['price'] = temp[f'store{i}']
        final.append(ret)
    
    return pd.concat(final, axis=0, ignore_index=True)