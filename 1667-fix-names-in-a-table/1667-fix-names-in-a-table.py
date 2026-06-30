import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Use the .str.capitalize() method to make the first letter uppercase 
    # and the rest lowercase.
    users['name'] = users['name'].str.capitalize()
    
    # Sort the DataFrame by 'user_id' in ascending order and reset the index
    return users.sort_values(by='user_id').reset_index(drop=True)