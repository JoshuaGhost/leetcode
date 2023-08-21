import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity[activity['activity_date'].between('2019-06-28', '2019-07-27')]
        .groupby('activity_date', as_index=False)
        .nunique('user_id')
        .rename({'activity_date': 'day', 'user_id': 'active_users'}, axis=1)[['day', 'active_users']]
    )