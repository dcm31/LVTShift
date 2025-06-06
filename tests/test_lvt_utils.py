import os
import sys
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lvt_utils import calculate_current_tax, model_split_rate_tax


def test_calculate_current_tax_basic():
    df = pd.DataFrame({
        'tax_val': [100, 200, 300],
        'millage': [10, 10, 10]
    })
    total_rev, second_rev, result = calculate_current_tax(df, 'tax_val', 'millage')
    assert pytest.approx(total_rev) == 6
    assert second_rev == 0
    assert list(result['current_tax']) == [1.0, 2.0, 3.0]


def test_model_split_rate_tax_revenue_neutral():
    df = pd.DataFrame({
        'land': [100, 100],
        'improvement': [100, 300]
    })
    current_rev = 4.0
    land_rate, imp_rate, new_rev, result = model_split_rate_tax(
        df, 'land', 'improvement', current_rev, land_improvement_ratio=4
    )
    assert pytest.approx(new_rev) == current_rev
    assert pytest.approx(imp_rate, rel=1e-4) == 3.3333333333
    assert pytest.approx(land_rate, rel=1e-4) == 13.3333333333
    assert list(result['new_tax']) == pytest.approx([1.6666667, 2.3333333])

