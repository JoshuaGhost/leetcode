import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['first'] = activity.groupby(by='player_id').event_date.transform(min)
    activity2 = activity[activity['first'] + pd.DateOffset(1) == activity['event_date']]
    return pd.DataFrame({'fraction': [round(len(activity2)/activity.player_id.nunique(), 2)]})
