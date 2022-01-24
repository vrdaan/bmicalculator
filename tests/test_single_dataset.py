import os
import sys
from bmicalculator.calculator import BmiCalculator

sys.path.append(os.path.dirname(os.getcwd()))


def test_single_dataset():
    updatedDataset = BmiCalculator().calculateSingleRowBmi(
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96}
    )
    assert type(updatedDataset) == dict
    assert len(updatedDataset) == 6
