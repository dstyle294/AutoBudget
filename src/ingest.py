import pandas as pd

def parse(
    csv_path: str
) -> pd.DataFrame:
    """Takes csv path and returns Pandas dataframe.

    Args:
        csv_path: Absolute or relative path to csv file with banking statement
    
    Returns:
        df: Pandas dataframe object for csv
    """
    df = pd.read_csv(csv_path, index_col=False)
    return df

