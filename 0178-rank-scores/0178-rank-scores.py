import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate the dense rank of the scores in descending order.
    # method='dense' ensures there are no gaps between ranks after ties.
    # We cast the result to integer since rank() returns floats by default.
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    
    # Sort the DataFrame by 'score' in descending order, 
    # select the required columns, and reset the index.
    return scores[['score', 'rank']].sort_values(by='score', ascending=False).reset_index(drop=True)