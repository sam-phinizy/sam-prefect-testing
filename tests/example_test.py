import pytest
import pandas as pd
from hello import count_countries_by_region

def test_count_countries_by_region_basic():
    data = {
        'Country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],
        'Region': ['North America', 'North America', 'North America', 'South America', 'South America']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert result['North America'] == 3
    assert result['South America'] == 2
    assert len(result) == 2

def test_count_countries_by_region_empty():
    df = pd.DataFrame(columns=['Country', 'Region'])
    result = count_countries_by_region(df)
    assert len(result) == 0

def test_count_countries_by_region_single_region():
    data = {
        'Country': ['France', 'Germany', 'Italy'],
        'Region': ['Europe', 'Europe', 'Europe']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert result['Europe'] == 3
    assert len(result) == 1

def test_count_countries_by_region_duplicate_countries():
    data = {
        'Country': ['USA', 'USA', 'Canada', 'Canada'],
        'Region': ['North America', 'North America', 'North America', 'North America']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)