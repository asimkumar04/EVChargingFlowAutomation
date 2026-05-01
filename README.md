# 🌍 API Automation Framework – Open Charge Map

This is a Python-based API automation framework using `pytest` for validating Open Charge Map APIs.

It covers:
- Reference Data API
- POI (Point of Interest) API

The framework validates:
✔ Functional correctness  
✔ Response time performance  
✔ Schema validation  
✔ Business rules  
✔ Data integrity  

It generates **HTML test reports** for execution results.

---

# ⚙️ Tech Stack

- Python  
- pytest  
- requests  
- python-dotenv  
- pytest-html  

---

# 📁 Project Structure

api-framework/
│
├── api/
│   ├── base_client.py
│   ├── referencedata_api.py
│   ├── poi_api.py
│
├── tests/
│   ├── test_referencedata.py
│   ├── test_poi.py
│
├── docs/
│   ├── EV_charging_system_flow.md
│
├── conftest.py
├── reports/
├── requirements.txt
└── README.md

---

# 🚀 How to Copy & Run from GitHub

## 1. Clone the Repository

Open terminal and run:

```bash id="clone_001"
git clone <your-github-repo-url>