# Streamlit RCA Dashboard – QA Project (Manual + Automation Testing)

This repository contains a complete Quality Assurance (QA) implementation for a Streamlit-based Root Cause Analysis (RCA) dashboard. The objective of this QA testing is to verify the functional correctness, data accuracy, usability, and stability of the RCA (Root Cause Analysis) Streamlit Dashboard. The testing effort ensures that core analytical workflows—file upload, RCA computation, filtering, comparison, and export—work reliably under valid, invalid, and edge-case scenarios. The project demonstrates both **manual testing fundamentals** and **Selenium-Pytest automation**, following industry-standard QA practices.

---

## 🔍 System Under Test (SUT)
A Streamlit-based RCA dashboard that allows users to:
- Upload KPI Excel files
- Validate required columns and data integrity
- Display KPIs and insights
- Comparison between two companies
- Download charts and reports

---

## 🧪 Manual Testing Artifacts
All manual testing deliverables are included to reflect a real-world QA workflow:

- **Test Plan** – Scope, objectives, entry/exit criteria, risks
- **Test Scenarios & Test Cases** – Functional and UI validations
- **Bug Reports** – Documented defects with steps to reproduce and severity
- **UI Checklist** – Layout, responsiveness, error messages
- **Requirement Traceability Matrix (RTM)** – Mapping requirements to test cases

📁 Location:
Rca Dashboard Qa – Test Plan & Initial Test Cases
Rca Dashboard Qa – Test Plan & Initial Test Cases


---

## 🤖 Automation Testing
Automation is implemented using **Selenium + Pytest** following the **Page Object Model (POM)** design pattern.

### Automated Scenarios
- Valid KPI file upload
- Invalid file upload (missing required columns)
- Error message validation
- Segment filter verification
- UI element presence checks

### Tech Stack
- Python 3.10
- Selenium WebDriver
- Pytest
- Pytest-HTML (report generation)
- ChromeDriver


---

## ▶️ How to Run Automation Tests
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -v --html=report.html



