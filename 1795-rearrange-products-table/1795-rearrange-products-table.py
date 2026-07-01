import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Use melt() to transform the DataFrame from wide format to long format.
    # id_vars are the columns to keep as identifiers.
    # value_vars are the columns to unpivot into rows.
    # var_name and value_name specify the new column names for the unpivoted data.
    melted = products.melt(
        id_vars=['product_id'], 
        value_vars=['store1', 'store2', 'store3'], 
        var_name='store', 
        value_name='price'
    )
    
    # Drop rows where the price is null (meaning the product is not available in that store)
    result = melted.dropna(subset=['price'])
    
    return result