import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
     # N must be a positive integer to represent the Nth highest salary.
    # If N <= 0, it's an invalid rank, so we return null.
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
        
    # Get distinct salaries and sort them in descending order
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are at least N distinct salaries
    if len(distinct_salaries) >= N:
        # Get the N-th highest salary (which is at index N-1)
        nth_salary = distinct_salaries.iloc[N - 1]
    else:
        # If there are fewer than N distinct salaries, return None (null)
        nth_salary = None
        
    # Create and return the result DataFrame with the specified column name
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})