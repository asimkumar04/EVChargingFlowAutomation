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

It generates **HTML test reports** with timestamp under report folder for execution results.

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

├── api/
   base_client.py
   referencedata_api.py
   poi_api.py

├── tests/
   test_referencedata_api.py
   test_poi_api.py

├── docs/
   EV_charging_system_flow.md

├── conftest.py
├── reports/
├── requirements.txt
└── README.md

---

# 🚀 How to Copy & Run from GitHub

1️ Clone the Repository
git clone https://github.com/asimkumar04/EVChargingFlowAutomation.git
cd EVChargingFlowAutomation
2️ Install Dependencies
pip install -r requirements.txt
3️ Run the Application
python main.py
4. Run tests using:
pytest

# 🔐 How to Properly Get an API Authentication Key
To get a valid api key visit the Web URL and inspect the API calls triggered. On the request headers of the
API calls pointing to the mentioned base url you will find a valid Api key to use for your requests. Replace the
same in .env file
