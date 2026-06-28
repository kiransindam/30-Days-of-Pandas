import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame for products that are both low fat and recyclable
    condition = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    
    # Select and return only the 'product_id' column
    return products[condition][['product_id']]