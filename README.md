# Centralized Blockchain Web App

🚀 A **centralized blockchain-based web application** built using **FastAPI**.  
This project demonstrates how blockchain concepts such as immutability, hashing, and validation can be applied in a **centralized environment**, useful for learning, prototyping, and academic purposes.

---

## 📌 Problem Statement
The rise of data tampering and lack of transparency in record management highlight the need for a **secure, verifiable system**. Traditional centralized databases are fast but vulnerable to manipulation.  
This project explores how blockchain principles can **strengthen centralized systems** by ensuring:
- Data immutability  
- Tamper detection  
- Transparent validation  

---

## ✅ Proposed Solution
We implemented a **centralized blockchain system** with the following features:
- A single server maintains the blockchain ledger.  
- Each block is cryptographically linked to the previous block.  
- Any attempt to tamper with data breaks the chain integrity.  
- Accessible through **REST APIs** and a simple frontend.  

This provides a learning model before extending to a **fully decentralized blockchain network**.

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python 3)
- **Database:** SQLite (or in-memory fallback)
- **Frontend:** HTML, CSS, JavaScript
- **Server:** Uvicorn (ASGI server)

---
## 📂 Project Structure
blockchain-students/<br>
├── requirements.txt          # Project dependencies <br>
├── app/
│   ├── main.py              # FastAPI application entry point <br>
│   ├── database.py          # Database configuration and connection <br>
│   ├── models.py            # SQLAlchemy ORM models <br>
│   ├── schemas.py           # Pydantic schemas for data validation <br>
│   └── blockchain.py        # Core blockchain implementation <br>
└── static/<br>
    ├── index.html           # Web interface <br>
    └── app.js               # Frontend JavaScript logic <br>

---

## 📋 Prerequisites
Before running the application, make sure you have the following installed on your system:

- **Python 3.10+**  
- **pip** (Python package manager)  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/atharv-thakre/centralized_blockchain.git
cd centralized_blockchain
```
### 2️⃣ Create virtual environment (optional but recommended)
- windows
```bash
python -m venv venv
venv\Scripts\activate
```

- mac / linux
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python -m uvicorn app.main:app --reload
```

---


## 🌐 Usage
Open browser and go to:
👉 http://127.0.0.1:8000/

API Documentation available at:
👉 http://127.0.0.1:8000/docs

---

## ✨ Features
- Centralized blockchain ledger  
- FastAPI-powered REST APIs  
- Tamper-proof data validation  
- Simple frontend interface  
- Live API docs with Swagger  



