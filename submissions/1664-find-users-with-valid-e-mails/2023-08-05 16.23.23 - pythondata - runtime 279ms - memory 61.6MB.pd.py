import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z_.\-0-9]*@leetcode\.com$')]