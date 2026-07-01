import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Group by 'email' and find the minimum 'id' for each unique email
    min_ids = person.groupby('email')['id'].min()
    
    # Identify the rows to keep (where the 'id' is the minimum for its email)
    # and drop the remaining duplicate rows in place
    person.drop(person[~person['id'].isin(min_ids)].index, inplace=True)