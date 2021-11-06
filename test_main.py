from utils import BMICalculator
import pytest
from exception import HeightNullError, WeightNullError, HeightLessThanZeroError, WeightLessThanZeroError


def test_bmi_calculator_less_than_18():
    obj = BMICalculator("Male", 150, 36)
    bmi = obj.calculate_bmi()
    assert bmi == 16


def test_bmi_calculator_between_18and40():
    obj = BMICalculator("Male", 175, 100)
    bmi = obj.calculate_bmi()
    assert bmi == 32.65


def test_bmi_calculator_between_more_than_40():
    obj = BMICalculator("Male", 170, 130)
    bmi = obj.calculate_bmi()
    assert bmi == 44.98


def test_bmi_calculator_between_height_null():
    with pytest.raises(HeightNullError) as exec_info:
        obj = BMICalculator("Male", '', 130)
    assert str(exec_info.value) == "Value of height cannot be Null"


def test_bmi_calculator_between_weight_null():
    with pytest.raises(WeightNullError) as exec_info:
        obj = BMICalculator("Male", 170, '')
    assert str(exec_info.value) == "Value of weight cannot be Null"


def test_bmi_calculator_between_height_less_than_zero():
    with pytest.raises(HeightLessThanZeroError) as exec_info:
        obj = BMICalculator("Male", -100, 130)
    assert str(exec_info.value) == "Value of height cannot be zero or less than zero"


def test_bmi_calculator_between_weight_less_than_zero():
    with pytest.raises(WeightLessThanZeroError) as exec_info:
        obj = BMICalculator("Male", 170, -5)
    assert str(exec_info.value) == "Value of weight cannot be zero or less than zero"
