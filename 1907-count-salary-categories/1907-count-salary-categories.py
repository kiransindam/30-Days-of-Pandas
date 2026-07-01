import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
     # Calculate the count for each category using boolean conditions
    low_count = (accounts['income'] < 20000).sum()
    avg_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()
    
    # Construct the result DataFrame ensuring all three categories are present
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, avg_count, high_count]
    })
    
    return result