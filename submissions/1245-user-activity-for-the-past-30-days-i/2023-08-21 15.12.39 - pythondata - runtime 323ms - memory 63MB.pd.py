import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity[
            (activity['activity_date'] <= pd.to_datetime('2019-07-27')) &
            (activity['activity_date'] > pd.to_datetime('2019-07-27') - pd.DateOffset(30))
            ]
        .groupby('activity_date', as_index=False)
        .nunique('user_id')
        .rename({'activity_date': 'day', 'user_id': 'active_users'}, axis=1)[['day', 'active_users']]
        .sort_values('day')
    )