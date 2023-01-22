import math
import C_c_validation


def test_sum_odd_digits():
    assert math.sum_odd_digits(4187_4515_2106_5526) == "INVALID" "VALID"


def test_sum_even_digits():
    assert math.sum_even_digits(2347_9876_2408_6687) == "INVALID" or "VALID"
