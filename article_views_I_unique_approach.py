import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # condition 
    df = views[
        views['author_id'] == views['viewer_id']
    ]

    # get unique columns
    df = df['author_id'].unique() # this will be an array 

    # convert df to dataframe
    df = pd.DataFrame(df, columns = ['id']) # convert df array to datatframe

    # sort the values
    df.sort_values(by = ['id'], inplace = True)

    return df 

