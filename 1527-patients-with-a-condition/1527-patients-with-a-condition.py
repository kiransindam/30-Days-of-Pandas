import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
        condition = patients['conditions'].str.contains(r'^DIAB1| DIAB1', na=False)
        return patients[condition]