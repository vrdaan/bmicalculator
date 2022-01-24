import os
import sys
from bmicalculator.calculator import BmiCalculator

sys.path.append(os.path.dirname(os.getcwd()))


def test_multi_dataset():
    updateJson = BmiCalculator().calculateBmi([
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ])
    assert len(updateJson) == 6
    assert len(updateJson[0].keys()) == 6