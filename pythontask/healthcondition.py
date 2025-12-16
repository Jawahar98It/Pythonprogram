ideal_patient_data = {
    "sugar_level": 75,
    "blood_pressure": 110,
    "heart_rate": 70,
    "weight": 70,
    "fat_percentage": 15
}

def health_condition_check(patient_data, ideal_data):
    report = {}

    for key in ideal_data:
        if key in patient_data:
            if patient_data[key] < ideal_data[key]:
                report[key] = "Low"
            elif patient_data[key] > ideal_data[key]:
                report[key] = "High"
            else:
                report[key] = "Normal"
        else:
            report[key] = "Data not provided"

    return report

# Patient input
patient_data = {
    "sugar_level": int(input("Enter sugar level: ")),
    "blood_pressure": int(input("Enter blood pressure: ")),
    "heart_rate": int(input("Enter heart rate: ")),
    "weight": int(input("Enter weight: ")),
    "fat_percentage": int(input("Enter fat percentage: "))
}

condition_report = health_condition_check(patient_data, ideal_patient_data)

print("\nHealth Condition Report:")
for key, value in condition_report.items():
    print(f"{key}: {value}")
