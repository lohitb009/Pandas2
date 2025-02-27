import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # condition 
    df = views[
        views['author_id'] == views['viewer_id']
    ]

    # remove the duplicates
    # inplace = True means that make modification in the same dataframe df
    # inplace = False means that we will store in a new dataframe
    df_1 = df.drop_duplicates(subset = ["author_id"], inplace = False) # on which column to drop the duplicates

    # sort the values
    df_1.sort_values(by = ["author_id"], inplace = True)

    # pick up author id column
    return df_1[["author_id"]].rename(columns = {'author_id' : 'id'})