# 🧪 API-Project

This project is an automated test suite for a RESTful Booking API, using Python, Behave (BDD), and Allure for reporting. It covers key operations like authentication, booking creation, update, deletion, and partial updates.

---

## 🚀 Features

- ✅ Token-based Authentication
- 📝 Booking Creation (POST)
- 🔍 Booking Retrieval (GET by ID)
- 🧾 Booking Update (PUT & PATCH)
- ❌ Booking Deletion
- 🔐 Auth Validation (Bad Credentials, Missing Token)
- 📊 Allure Report Generation
- 📁 Modular structure with reusable payload and config files

---

## 🧰 Tech Stack

- Python 3.x
- Behave (BDD framework)
- Requests (for HTTP calls)
- Allure (reporting)
- JSON config and payloads

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/nafis08/API-Project.git
cd API-Project
```
Create virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Running Tests
```bash
behave
or
behave feature/filename.feature #example: behave feature/createBookingAPI.feature #For running specific test 
```
Generating Allure Report
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features
allure generate reports/allure-results -o reports/allure-report --clean
open reports/allure-report/index.html  
```
🧪 Sample API Modules
--> API_createBooking.py — creates a new booking

--> API_updateBooking.py — updates booking via PUT

--> API_partialUpdate.py — updates via PATCH

--> API_tokenCreation.py — retrieves a token

--> API_deleteAPI.py - deletes a booking

📁 Project Structure
graphql
API-Project/
├── features/                 # BDD feature files & step definitions
├── util_package/            # Config & utility functions
├── reports/                 # Allure reports output
├── .venv/                   # Virtual environment
├── *.py                     # API operation scripts
├── *.json                   # Credentials & payload templates
└── README.md

