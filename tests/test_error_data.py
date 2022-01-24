import os
import sys
from bmicalculator.calculator import BmiCalculator

sys.path.append(os.path.dirname(os.getcwd()))


def test_multi_dataset():
    updateJson = BmiCalculator().calculateBmi([
        {"Gender": "Male", "HeightCm": "test", "WeightKg": 96},
        {"Gender": "Male", "HeightCm": None, "WeightKg": 85},
    ])
    assert len(updateJson) == 2
    assert len(updateJson[0].keys()) == 6
    for keys in ['BMI', 'Category', 'Health Risk']:
        assert updateJson[0].get(keys) == False
        assert updateJson[1].get(keys) == False
