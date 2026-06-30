import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
       # Create a boolean mask for the conditions:
    # 1. employee_id is odd (modulo 2 is not 0)
    # 2. name does not start with 'M'
    condition = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    
    # Calculate the bonus: multiplying the boolean mask by the salary 
    # results in the salary where True, and 0 where False.
    employees['bonus'] = condition * employees['salary']
    
    # Select the required columns, sort by employee_id, and reset the index
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id').reset_index(drop=True)