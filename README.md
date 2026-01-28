📌 Project Title  Google-Sheets-MySQL-Live-Bidirectional-Sync-Platform
🚀 This project implements a production-grade, real-time, bidirectional data synchronization system between Google Sheets and a MySQL database.

Any change made in Google Sheets or MySQL is propagated to the other system with:
Conflict resolution
Idempotent writes
Schema flexibility
Multiplayer-safe handling
The system is designed as a stateless sync engine, making it suitable for scaling to large datasets and concurrent users.

🎯 Problem Statement
Build a system that:
Maintains live 2-way sync between Google Sheets and MySQL
Works for any table structure
Handles concurrent edits
Is production-ready, not a toy project
Provides a simple interface to test behavior in real time

🧠 Architecture of the project : 
Google Sheets (Apps Script Trigger)
        ↓
FastAPI Sync Engine
        ↓
MySQL Database
        ↑
(Optional MySQL Change Capture)

Key Principles : 
FastAPI acts as the single conflict-resolution authority
All writes are idempotent
Sync logic is timestamp-based
UI is stateless and used only for simulation and observability

🏗️ Tech Stack
Layer	                                  Technology
Backend                             API	FastAPI (Python)
Database                                 	MySQL
ORM	                                   SQLAlchemy
Sheet Integration               	Google Apps Script
UI	                      HTML + CSS + JS (single-file dashboard)
Conflict Handling	           Timestamp-based (Last-write-wins)


🔄 Sync Strategy : 
Row Identity
Every row is identified by a UUID
Same UUID = same logical record across systems
Conflict Resolution
Each update carries an updated_at timestamp
Newer timestamp wins
Older updates are safely ignored
Idempotency
Duplicate events do not corrupt data
Replayed events are safe.

📂Project Structure:
sheet-mysql-sync/
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── database.py        # DB connection
│   ├── models.py          # Sync state model
│   ├── sync_engine.py     # Conflict resolution logic
│   ├── ui.py              # Live dashboard UI
│   ├── sheet_client.py    # (Extensible)
│   └── mysql_listener.py  # (Extensible)
│
├── test_db.py
├── requirements.txt
└── README.md

🧪 Live Testing Interface : 
The system includes a professional internal dashboard that allows:
Manual mutation of UUID, name, email, and timestamps
Real-time sync simulation
Payload inspection
System action visibility
This UI is intentionally lightweight and stateless, mimicking internal tooling used by engineering teams.

⚙️How to Run Locally
1. Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1

2.Install Dependencies
pip install -r requirements.txt

3.Start Server
uvicorn app.main:app --reload

4.Open Dashboard
http://127.0.0.1:8000/


📊 Database Schema
users
uuid CHAR(36) PRIMARY KEY
name VARCHAR(255)
email VARCHAR(255)
updated_at TIMESTAMP

sync_state
uuid CHAR(36) PRIMARY KEY
source ENUM('SHEET','MYSQL')
updated_at TIMESTAMP
deleted BOOLEAN

🔐 Production Considerations :
Stateless API enables horizontal scaling
Can integrate Kafka / PubSub for large-scale event streaming
Conflict resolution logic isolated for extensibility
Safe for concurrent Google Sheet editors.

🏁 Conclusion

This project demonstrates:
Real-world sync engine design.
Safe handling of concurrent edits.
Production-quality backend thinking.
Clean separation of concerns.
It is intentionally built to resemble internal infrastructure tools, not demo-only code.
