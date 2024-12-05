import pytest
from data_processing import clean_data
import pandas as pd

def test_clean_data():
    df = pd.DataFrame({'col1': [1, 2, None], 'col2': [None, 1, 1]})
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0

if __name__ == '__main__':
    pytest.main()
