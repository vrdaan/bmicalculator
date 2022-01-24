from concurrent.futures import ThreadPoolExecutor
from pprint import pprint


class BmiCalculator:
    def __init__(self):
        self.totalOverWeight = 0
        self.data = []

    def chcekAllParam(func):
        def insiderFunc(*args, **kwargs):
            data = args[1]
            if (w := data.get('WeightKg')) is not None and (h := data.get('HeightCm')) is not None:
                print(w,h)
                try:
                    float(w), float(h)
                    returned_value = func(*args, **kwargs)
                    return returned_value
                except ValueError:
                    data.update({'BMI': False, 'Category': False, 'Health Risk': False})
            else:
                data.update({'BMI': False, 'Category': False, 'Health Risk': False})

        return insiderFunc

    @chcekAllParam
    def _calcuateBmi(self, row: dict) -> None:
        heightInM = float(row.get('HeightCm')) / 100
        bmi = float(row.get('WeightKg')) / (heightInM * heightInM)
        if bmi < 18.4:
            weight = 'Underweight'
            risk = 'Malnutrition risk'
        elif 18.5 <= bmi < 24.9:
            weight = "Normal weight"
            risk = 'Low Risk'
        elif 25 <= bmi < 29.9:
            self.totalOverWeight += 1
            weight = 'Overweight'
            risk = 'Enhanced Risk'
        elif 30 <= bmi < 34.9:
            weight = 'Moderately obese'
            risk = 'Medium Risk'
        elif 35 <= bmi < 39.9:
            weight = 'Seriously obese'
            risk = 'High Risk'
        else:
            weight = 'Very Seriously obese'
            risk = 'Very High Risk'
        row.update({'BMI': bmi, 'Category': weight, 'Health Risk': risk})

    def calculateBmi(self, data: list) -> list:
        """Bmi Calculate for Multi Dataset Using Thread
        The ThreadPool automatically Iterate the list and update the data"""
        with ThreadPoolExecutor() as executor:
            result = executor.map(self._calcuateBmi, data)
        return data

    def calculateSingleRowBmi(self, row: dict) -> dict:
        """Bmi Calculate for Single Dataset"""
        self._calcuateBmi(row)
        return row

    def getTotalOverWeight(self) -> int:
        return self.totalOverWeight


if __name__ == '__main__':
    pass
    # bmi = BmiCalculator()
    # data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    #         {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    #         {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    #         {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    #         {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    #         {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
    #         {"Gender": "Male", "HeightCm": 173, "WeightKg": 96},
    #         {"Gender": "Male", "HeightCm": 164, "WeightKg": 85},
    #         {"Gender": "Male", "HeightCm": 181, "WeightKg": 71},
    #         {"Gender": "Female", "HeightCm": 163, "WeightKg": 64},
    #         {"Gender": "Female", "HeightCm": 1230, "WeightKg": 72},
    #         {"Gender": "Female", "HeightCm": 166, "WeightKg": 81}
    #         ]
    # pprint(bmi.calculateBmi(data))
    # print(bmi.getTotalOverWeight())
