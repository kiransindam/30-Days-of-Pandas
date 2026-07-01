import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the time spent in the office for each single entry
    employees['total_time'] = employees['out_time'] - employees['in_time']
    
    # Group by 'event_day' and 'emp_id', then sum the 'total_time'
    result = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    
    # Rename 'event_day' to 'day' to match the expected output format
    return result.rename(columns={'event_day': 'day'})