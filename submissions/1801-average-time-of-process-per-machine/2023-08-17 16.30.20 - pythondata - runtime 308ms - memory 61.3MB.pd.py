import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    temp = (
        activity
        .pivot(index=['machine_id', 'process_id'], columns='activity_type', values='timestamp')
        .reset_index()
    )
    temp['diff'] = temp['end'] - temp['start']
    return (
        temp
        .groupby(by=['machine_id'], as_index=False)
        .agg('mean')[['machine_id', 'diff']]
        .rename({'diff': 'processing_time'}, axis=1)
        .round(3)
    )
