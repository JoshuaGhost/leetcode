import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z_.\-0-9]*@leetcode\.com$')
    return users[users['mail'].str.match(pattern)]