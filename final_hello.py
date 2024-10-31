import pandas as pd
from prefect import flow, task
from pydantic import BaseModel
from pydantic import HttpUrl


class RegionCount(BaseModel):
    region_name: str
    count: int

class RegionCountList(BaseModel):
    regions: list[RegionCount]


@task
def load_countries_data(url: HttpUrl):
    return pd.read_csv(url)

@task
def count_countries_by_region(df: pd.DataFrame):
    return df.groupby('Region')['Country'].count()

@flow
def main_flow():
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
    countries_data = load_countries_data(url=url)
    region_counts = count_countries_by_region(countries_data)
    result = [RegionCount(region_name=str(region), count=int(count)) for region, count in region_counts.items()]
    return RegionCountList(regions=result).model_dump_json()


if __name__ == "__main__":
    print(main_flow())






