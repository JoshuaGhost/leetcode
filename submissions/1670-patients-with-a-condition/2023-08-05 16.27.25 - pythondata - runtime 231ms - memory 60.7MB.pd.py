import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = re.compile(r'.*\bDIAB1\w+\b.*')
    return patients[patients.conditions.str.match(pattern)]