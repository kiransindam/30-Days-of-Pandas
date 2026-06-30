import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to find rows where the author is also the viewer
    self_views = views[views['author_id'] == views['viewer_id']]
    
    # Select the 'author_id' column, drop duplicates, and rename it to 'id'
    result = self_views[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})
    
    # Sort the result by 'id' in ascending order and reset the index
    return result.sort_values(by='id').reset_index(drop=True)