import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity[['player_id', 'event_date']].groupby(by='player_id', as_index=False).min().rename({'event_date': 'first_login'}, inplace=False, axis=1)
