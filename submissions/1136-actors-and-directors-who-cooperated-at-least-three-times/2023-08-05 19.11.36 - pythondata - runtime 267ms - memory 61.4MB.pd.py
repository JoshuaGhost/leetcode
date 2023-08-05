import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    temp = actor_director.groupby(['actor_id', 'director_id'], as_index=False).count()
    return temp[temp['timestamp'] >= 3][['actor_id', 'director_id']]