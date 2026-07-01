import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:# Rename columns to match the expected output and avoid naming conflicts during merge
    emp = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    dep = department.rename(columns={'name': 'Department'})
    
    # Merge the Employee and Department tables
    merged = emp.merge(dep, left_on='departmentId', right_on='id')
    
    # Calculate the maximum salary for each department using transform
    max_salary = merged.groupby('Department')['Salary'].transform('max')
    
    # Filter the DataFrame to keep only the employees with the highest salary in their department
    result = merged[merged['Salary'] == max_salary][['Department', 'Employee', 'Salary']]
    
    return result
    