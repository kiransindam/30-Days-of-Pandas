import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
     # Get distinct salaries and sort them in descending order
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are at least 2 distinct salaries
    if len(distinct_salaries) >= 2:
        # Get the second highest salary (which is at index 1)
        second_highest = distinct_salaries.iloc[1]
    else:
        # If there are fewer than 2 distinct salaries, return None (null)
        second_highest = None
        
    # Create and return the result DataFrame with the specified column name
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})