CHECKLIST = [
    "Articles of Association",
    "Consent to Act",
    "Data Protection Declaration",
    "Fit & Proper Declaration",
    "Name Declaration",
    "Passport Summary",
    "Nominee Confirmations",
    "Resolution of Incorporating Shareholders",
    "UBO Declaration Form",
    "Business Plan",
    "Source of Wealth"
]

def check_compliance(text):
    missing = [item for item in CHECKLIST if item.lower() not in text.lower()]
    return missing