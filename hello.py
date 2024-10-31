import pandas as pd
from prefect import task, flow

@task
def fetch_countries_data() -> pd.DataFrame:
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
    return pd.read_csv(url)

@task
def count_countries_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Region')['Country'].count()

@flow
def region_count_flow():
    df = fetch_countries_data()
    counts = count_countries_by_region(df)
    print(counts)
    return counts

if __name__ == "__main__":
    region_count_flow()
