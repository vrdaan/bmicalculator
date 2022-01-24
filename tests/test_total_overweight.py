import os
import sys
from bmicalculator.calculator import BmiCalculator

sys.path.append(os.path.dirname(os.getcwd()))


def test_total_overweight():
    bmiObj = BmiCalculator()
    bmiObj.calculateBmi([
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ])
    overWeigth = bmiObj.getTotalOverWeight()
    assert type(overWeigth) == int
    assert overWeigth == 1
