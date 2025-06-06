import pandas as pd
import os
from webapp.app import load_dataset

def test_load_dataset_from_file(tmp_path):
    csv_path = tmp_path / 'data.csv'
    csv_path.write_text('a,b\n1,2\n')
    df = load_dataset(None, str(csv_path))
    assert list(df.columns) == ['a', 'b']


def test_load_dataset_from_upload(tmp_path):
    csv_path = tmp_path / 'data2.csv'
    csv_path.write_text('x,y\n3,4\n')
    with open(csv_path, 'rb') as f:
        df = load_dataset(f, None)
    assert 'x' in df.columns


def test_load_dataset_no_input():
    try:
        load_dataset(None, None)
    except ValueError:
        pass
    else:
        assert False, 'ValueError not raised'
