import pytest
import pandas as pd
from hello import count_countries_by_region

def test_count_countries_by_region_mixed_case():
    data = {
        'Country': ['USA', 'Canada', 'Mexico'],
        'Region': ['North America', 'north america', 'NORTH AMERICA']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert len(result) == 3
    assert result['North America'] == 1
    assert result['north america'] == 1
    assert result['NORTH AMERICA'] == 1

def test_count_countries_by_region_special_chars():
    data = {
        'Country': ['Country1', 'Country2', 'Country3'],
        'Region': ['Region-1', 'Region#2', 'Region 3']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert len(result) == 3
    assert result['Region-1'] == 1
    assert result['Region#2'] == 1
    assert result['Region 3'] == 1

def test_count_countries_by_region_null_values():
    data = {
        'Country': ['USA', 'Canada', None, 'Mexico'],
        'Region': ['North America', 'North America', 'North America', None]
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert len(result) == 2
    assert result['North America'] == 3
    assert pd.isna(result.index[-1])
    assert result.iloc[-1] == 1


def test_count_countries_by_region_empty_dataframe():
    df = pd.DataFrame(columns=['Country', 'Region'])
    result = count_countries_by_region(df)
    assert len(result) == 0


def test_count_countries_by_region_single_region():
    data = {
        'Country': ['USA', 'Canada', 'Mexico'],
        'Region': ['North America', 'North America', 'North America']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert len(result) == 1
    assert result['North America'] == 3


def test_count_countries_by_region_duplicate_countries():
    data = {
        'Country': ['USA', 'USA', 'Canada', 'Canada'],
        'Region': ['North America', 'North America', 'North America', 'North America']
    }
    df = pd.DataFrame(data)
    result = count_countries_by_region(df)
    assert len(result) == 1
    assert result['North America'] == 4
