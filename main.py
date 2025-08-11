from doc_processor import extract_text, insert_comments
from compliance import check_compliance
from rag_processor import build_vectorstore, generate_clause_suggestion
from report import generate_report

INPUT_FILE = "input.docx"
ANNOTATED_FILE = "annotated_output.docx"
REPORT_FILE = "report.json"

def main():
    print("[*] Reading user document...")
    text = extract_text(INPUT_FILE)

    print("[*] Checking for missing compliance items...")
    missing_items = check_compliance(text)

    print("[*] Inserting comments into document...")
    insert_comments(INPUT_FILE, ANNOTATED_FILE, missing_items)

    print("[*] Building RAG knowledge base from ADGM docs...")
    vectorstore = build_vectorstore("adgm_docs")

    print("[*] Generating clause suggestions...")
    suggestions = {}
    for item in missing_items:
        print(f" → Generating for: {item}")
        suggestions[item] = generate_clause_suggestion(item, vectorstore)

    print("[*] Creating summary report...")
    generate_report(missing_items, suggestions, REPORT_FILE)

    print("\n✅ Done!")
    print(f"• Annotated: {ANNOTATED_FILE}")
    print(f"• Report: {REPORT_FILE}")

if _name_ == "_main_":
    main()