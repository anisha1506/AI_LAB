# knowledge_base.py

rules = [
    {
        "symptoms": {"chest pain", "shortness of breath"},
        "diagnosis": "Possible Heart Attack",
        "department": "Cardiology",
        "urgency": "Emergency",
        "facility": "ICU"
    },
    {
        "symptoms": {"fever", "cough", "fatigue"},
        "diagnosis": "Suspected Flu or COVID-19",
        "department": "General Medicine",
        "urgency": "Routine",
        "facility": "OPD"
    },
    {
        "symptoms": {"severe headache", "blurred vision", "confusion"},
        "diagnosis": "Possible Stroke",
        "department": "Neurology",
        "urgency": "Emergency",
        "facility": "ER"
    },
    {
        "symptoms": {"abdominal pain", "nausea", "vomiting"},
        "diagnosis": "Suspected Gastroenteritis",
        "department": "Gastroenterology",
        "urgency": "Urgent",
        "facility": "OPD"
    }
]
