import json

def generate_report(missing_docs, clause_suggestions, output_path="report.json"):
    report = {
        "status": "incomplete" if missing_docs else "complete",
        "missing_documents": missing_docs,
        "clause_suggestions": clause_suggestions
    }
    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)
    print(f"[✓] Report saved to {output_path}")