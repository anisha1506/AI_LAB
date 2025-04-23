
from knowledge_base import rules

def infer(symptom_input):
    symptom_set = set(symptom_input.lower().split(', '))
    for rule in rules:
        if rule["symptoms"].issubset(symptom_set):
            return {
                "Diagnosis": rule["diagnosis"],
                "Department": rule["department"],
                "Urgency": rule["urgency"],
                "Facility": rule["facility"]
            }
    return {
        "Diagnosis": "Uncommon condition.",
        "Department": "General Medicine",
        "Urgency": "Routine",
        "Facility": "OPD"
    }

if __name__ == "__main__":
    print("*************Welcome to the Hospital & Medical Facility Expert System**********************")
    symptoms = input("Enter your symptoms (comma-separated): ")
    result = infer(symptoms)
    print("\n--- Medical Recommendation ---")
    for key, value in result.items():
        print(f"{key}: {value}")
