import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define the regex pattern for a valid email:
    # ^[a-zA-Z]         : The prefix must start with a letter
    # [a-zA-Z0-9_.-]*   : Followed by zero or more allowed characters (letters, digits, '_', '.', '-')
    # @leetcode\.com$   : Must end with the exact domain '@leetcode.com'
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    
    # Filter the DataFrame using str.match()
    # na=False ensures that NaN values do not cause errors and are treated as non-matches
    valid_users = users[users['mail'].str.match(pattern, na=False)]
    
    return valid_users