import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame for countries that meet either condition
    condition = (world['area'] >= 3000000) | (world['population'] >= 25000000)
    big_countries_df = world[condition]
    
    # Select and return only the required columns
    return big_countries_df[['name', 'population', 'area']]