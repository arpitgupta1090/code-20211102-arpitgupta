from utils import BMICalculator

table1 = [
    {"BMI Category": "Underweight", "BMI Range": 18.4, "Health risk": "below Malnutrition risk"},
    {"BMI Category": "Normal weight", "BMI Range": 24.9, "Health risk": "Low risk"},
    {"BMI Category": "Overweight", "BMI Range": 29.9,  "Health risk": "Enhanced risk"},
    {"BMI Category": "Moderately obese", "BMI Range": 34.9, "Health risk": "Medium risk"},
    {"BMI Category": "Severely obese", "BMI Range": 39.9, "Health risk": "High risk"},
    {"BMI Category": "Very severely obese", "BMI Range": 40, "Health risk": "Very high risk"}
]

input_data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]


def add_bmi_category__health_risk(data_list, table):

    for data in data_list:
        obj = BMICalculator.create_from_raw_data(data)
        bmi = obj.calculate_bmi()
        category, health_risk = obj.bmi_category_health_risk(table)
        data["BMI"] = bmi
        data["BMI Category"] = category
        data["Health Risk"] = health_risk

    return data_list


def number_of_overweight(data_list, table):
    added_list = add_bmi_category__health_risk(data_list, table)
    overweight_list = [person for person in added_list if person["BMI Category"] == "Overweight"]
    return len(overweight_list)


if __name__ == "__main__":

    new_list = add_bmi_category__health_risk(input_data, table1)
    print(new_list)
    print(number_of_overweight(input_data, table1))

