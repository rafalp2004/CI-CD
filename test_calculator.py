import pytest

import calculator

@pytest.mark.parametrize("n, expected", [
    (0, "0"),
    (5, "101"),
    (10, "1010"),
    (100, "1100100"),
])
def test_to_binary_correct_conversion(n, expected):
    """Test green case"""
    assert calculator.to_binary(n) == expected


@pytest.mark.parametrize("n", [-1, 101])
def test_to_binary_out_of_range(n):
    """Test red case"""
    with pytest.raises(ValueError):
        calculator.to_binary(n)
