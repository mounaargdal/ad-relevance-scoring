import pandas as pd
from pathlib import Path

DATA_PATH = Path(_file_).resolve().parents[1] / "data" / "sample_ads.csv"

def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["query"] = df["query"].str.strip().str.lower()
    df["ad_title"] = df["ad_title"].str.strip()
    df["ad_text"] = df["ad_text"].str.strip()
    return df
