import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Filter out customers whose IDs are present in the 'customerId' column of the Orders table
    never_ordered = customers[~customers['id'].isin(orders['customerId'])]
    
    # Select the 'name' column and rename it to 'Customers' to match the expected output
    return never_ordered[['name']].rename(columns={'name': 'Customers'})