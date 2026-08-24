# build_workbook.py
# Requirements: pandas, openpyxl
# Install: pip install pandas openpyxl

import pandas as pd
from pathlib import Path

# Input CSV file
CSV_FILE = Path("matrix.csv")

# Output Excel file
OUTFILE = Path("PrivateMarkets_InvestmentControl_CompetitiveMatrix.xlsx")

# ---------- Load Competitive Matrix ----------
df_matrix = pd.read_csv(CSV_FILE, dtype=str)

# ---------- Sheet 2: Deep Dives ----------
deep_dives = [
    {
        "Vendor": "Canoe Intelligence",
        "A Extract": "YES - numeric and clause extraction from LP/GP docs",
        "B Validate": "PARTIAL - provenance and mismatch flags",
        "C Expected": "PARTIAL - no public evidence of full LPA modeling",
        "D Reconcile": "PARTIAL - dashboards show mismatches",
        "E Investigate": "PARTIAL - provenance links for manual review",
        "F Recommend": "PARTIAL - suggested actions in marketing",
        "G Execute": "PARTIAL - API pushes; no automated remediation shown",
        "Source": "https://canoeintelligence.com/product"
    },
    {
        "Vendor": "Juniper Square",
        "A Extract": "YES - call notices and allocations",
        "B Validate": "PARTIAL - rule checks, manual approvals",
        "C Expected": "NO - no automated LPA parsing",
        "D Reconcile": "PARTIAL - reconciliation features",
        "E Investigate": "NO - manual workflows",
        "F Recommend": "NO",
        "G Execute": "YES - payment and accounting integrations",
        "Source": "https://www.junipersquare.com/product"
    },
    {
        "Vendor": "Chronograph",
        "A Extract": "YES - call notice extraction",
        "B Validate": "YES - automated validation",
        "C Expected": "PARTIAL - limited modeling",
        "D Reconcile": "PARTIAL",
        "E Investigate": "PARTIAL",
        "F Recommend": "NO",
        "G Execute": "NO",
        "Source": "https://www.chronograph.io"
    },
    {
        "Vendor": "Allvue",
        "A Extract": "YES",
        "B Validate": "YES",
        "C Expected": "PARTIAL",
        "D Reconcile": "YES",
        "E Investigate": "PARTIAL",
        "F Recommend": "PARTIAL",
        "G Execute": "YES",
        "Source": "https://www.allvuesystems.com/solutions"
    },
    {
        "Vendor": "eFront",
        "A Extract": "YES",
        "B Validate": "YES",
        "C Expected": "PARTIAL",
        "D Reconcile": "YES",
        "E Investigate": "PARTIAL",
        "F Recommend": "PARTIAL",
        "G Execute": "YES",
        "Source": "https://www.blackrock.com/solutions/efront"
    },
    {
        "Vendor": "iLEVEL",
        "A Extract": "YES",
        "B Validate": "PARTIAL",
        "C Expected": "NO",
        "D Reconcile": "PARTIAL",
        "E Investigate": "PARTIAL",
        "F Recommend": "NO",
        "G Execute": "YES",
        "Source": "https://www.spglobal.com/marketintelligence/en/solutions/ilevel"
    },
    {
        "Vendor": "Dynamo",
        "A Extract": "YES",
        "B Validate": "PARTIAL",
        "C Expected": "NO",
        "D Reconcile": "PARTIAL",
        "E Investigate": "PARTIAL",
        "F Recommend": "NO",
        "G Execute": "YES",
        "Source": "https://www.dynamo.com/product"
    },
    {
        "Vendor": "Alkymi",
        "A Extract": "YES",
        "B Validate": "PARTIAL",
        "C Expected": "NO",
        "D Reconcile": "NO",
        "E Investigate": "PARTIAL",
        "F Recommend": "NO",
        "G Execute": "NO",
        "Source": "https://www.alkymi.io/solutions"
    },
    {
        "Vendor": "Ontra",
        "A Extract": "PARTIAL",
        "B Validate": "NO",
        "C Expected": "NO",
        "D Reconcile": "NO",
        "E Investigate": "NO",
        "F Recommend": "NO",
        "G Execute": "NO",
        "Source": "https://www.ontra.io/product"
    },
    {
        "Vendor": "DiligenceVault",
        "A Extract": "YES",
        "B Validate": "NO",
        "C Expected": "NO",
        "D Reconcile": "NO",
        "E Investigate": "NO",
        "F Recommend": "NO",
        "G Execute": "NO",
        "Source": "https://www.diligencevault.com/product"
    }
]

df_deep = pd.DataFrame(deep_dives)

# ---------- Sheet 3: Sources ----------
sources = [
    ("Canoe Intelligence", "https://canoeintelligence.com/product"),
    ("Juniper Square", "https://www.junipersquare.com/product"),
    ("Chronograph", "https://www.chronograph.io"),
    ("Allvue", "https://www.allvuesystems.com/solutions"),
    ("eFront", "https://www.blackrock.com/solutions/efront"),
    ("iLEVEL", "https://www.spglobal.com/marketintelligence/en/solutions/ilevel"),
    ("Dynamo", "https://www.dynamo.com/product"),
    ("Alkymi", "https://www.alkymi.io/solutions"),
    ("Ontra", "https://www.ontra.io/product"),
    ("DiligenceVault", "https://www.diligencevault.com/product"),
    ("Addepar", "https://www.addepar.com/product"),
    ("SS&C", "https://www.ssctech.com/solutions/fund-administration"),
    ("State Street", "https://www.statestreet.com/solutions/fund-services.html"),
    ("BNY Mellon", "https://www.bnymellon.com/us/en/what-we-do/investment-services/fund-services.jsp")
]

df_sources = pd.DataFrame(sources, columns=["Vendor", "URL"])

# ---------- Sheet 4: Verdict ----------
df_verdict = pd.DataFrame({
    "Question": [
        "Does this wedge represent meaningful whitespace?",
        "Single closest competitor?",
        "Most dangerous incumbent?",
        "Strongest initial customer segment?",
        "Strongest initial workflow?",
        "Would fund an MVP?"
    ],
    "Answer": [
        "Yes — end-to-end LPA+side-letter canonicalization + continuous expected-state evaluation is not publicly offered.",
        "Canoe Intelligence",
        "Allvue / eFront",
        "Family offices, endowments, OCIOs",
        "Capital-call verification + remaining-commitment reconciliation",
        "Yes, with a narrow MVP"
    ]
})

# ---------- Sheet 5: Scoring ----------
df_scoring = pd.DataFrame({
    "Category": [
        "Customer pain", "Competitive whitespace", "Technical feasibility",
        "Willingness to pay", "Go-to-market feasibility", "Defensibility",
        "Expansion potential", "Incumbent risk"
    ],
    "Score out of": [15, 15, 15, 10, 10, 15, 10, 10],
    "Score given": [12, 11, 11, 7, 6, 9, 8, 4]
})

# ---------- Sheet 6: Next Steps ----------
df_next = pd.DataFrame([
    ("Pilot scope", "Capital-call verification MVP for family offices and mid-sized endowments"),
    ("Data acquisition", "Secure NDAs and redacted LPAs/side letters for training data"),
    ("Integration plan", "Integrate with Allvue, Juniper Square, QuickBooks/Sage"),
    ("Auditability", "Design immutable provenance + human-in-the-loop approvals"),
    ("Pilot metrics", "Accuracy >95%, time saved, discrepancies detected, willingness to pay")
], columns=["Step", "Detail"])

# ---------- Write Excel Workbook ----------
with pd.ExcelWriter(OUTFILE, engine="openpyxl") as writer:
    df_matrix.to_excel(writer, sheet_name="Competitive Matrix", index=False)
    df_deep.to_excel(writer, sheet_name="Deep Dives", index=False)
    df_sources.to_excel(writer, sheet_name="Sources", index=False)
    df_verdict.to_excel(writer, sheet_name="Verdict", index=False)
    df_scoring.to_excel(writer, sheet_name="Scoring", index=False)
    df_next.to_excel(writer, sheet_name="Next Steps", index=False)

print(f"Workbook written to {OUTFILE.resolve()}")
