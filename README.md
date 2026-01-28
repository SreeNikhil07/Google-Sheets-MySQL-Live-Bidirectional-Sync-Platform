# 📌 Google-Sheets-MySQL-Live-Bidirectional-Sync-Platform

A **production-grade, real-time, bidirectional data synchronization platform** between **Google Sheets** and **MySQL**, designed with scalability, concurrency safety, and conflict resolution at its core.

This is **not a toy project** — it mirrors how internal sync engines are built in real-world systems.

---

## 🚀 Key Features

- 🔄 **Live 2-way synchronization** between Google Sheets and MySQL  
- 🧠 **Centralized conflict resolution** via FastAPI  
- ⏱️ **Timestamp-based Last-Write-Wins (LWW)** strategy  
- ♻️ **Idempotent writes** (safe retries & duplicate events)  
- 👥 **Multiplayer-safe** (handles concurrent edits gracefully)  
- 🧩 **Schema-flexible** (works for any table structure)  
- ⚙️ **Stateless sync engine** → horizontally scalable  
- 🧪 **Real-time internal dashboard** for testing & observability  

---

## 🎯 Problem Statement

Build a system that:

- Maintains **live bidirectional sync** between Google Sheets and MySQL  
- Works for **any table structure**  
- Handles **concurrent updates** without corruption  
- Is **production-ready**, not demo-only  
- Provides a **simple interface** to observe and test sync behavior  

---

Google Sheets (Apps Script Trigger)
↓
FastAPI Sync Engine
↓
MySQL Database
↑
(Optional MySQL Change Capture)

## 🧠 High-Level Architecture
<img width="896" height="538" alt="image" src="https://github.com/user-attachments/assets/cc0b1b75-99d3-45a2-a11f-a3ca3edf7c01" />



### 🔑 Design Principles

- **FastAPI is the single source of truth**
- All writes are **idempotent**
- **Timestamp-based conflict resolution**
- UI is **stateless**, used only for simulation & observability

---

## 🏗️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend API | FastAPI (Python) |
| Database | MySQL |
| ORM | SQLAlchemy |
| Sheets Integration | Google Apps Script |
| UI Dashboard | HTML + CSS + JavaScript (single-file) |
| Conflict Handling | Timestamp-based (Last-Write-Wins) |

---

## 🔄 Sync Strategy

### 🔐 Row Identity
- Every row is identified using a **UUID**
- Same UUID = same logical record across all systems

### ⚔️ Conflict Resolution
- Each update carries an `updated_at` timestamp
- **Newer timestamp wins**
- Older updates are ignored safely

### ♻️ Idempotency
- Duplicate or replayed events do **not corrupt data**
- Safe for retries and event reprocessing

---

## 📊 Database Schema

### `users` table
sql
uuid CHAR(36) PRIMARY KEY
name VARCHAR(255)
email VARCHAR(255)
updated_at TIMESTAMP

sync_table
uuid CHAR(36) PRIMARY KEY
source ENUM('SHEET','MYSQL')
updated_at TIMESTAMP
deleted BOOLEAN 

📂 Project Structure
sheet-mysql-sync/
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── database.py        # DB connection
│   ├── models.py          # ORM models
│   ├── sync_engine.py     # Conflict resolution logic
│   ├── ui.py              # Internal live dashboard
│   ├── sheet_client.py    # (Extensible) Google Sheets client
│   └── mysql_listener.py  # (Extensible) MySQL change capture
│
├── test_db.py
├── requirements.txt
└── README.md

🧪 Live Testing Dashboard

A professional internal dashboard is included to simulate real-world sync behavior.

Capabilities:

Manual mutation of:

UUID

name

email

timestamps

Real-time sync simulation

Payload inspection

Visibility into system decisions

This UI intentionally mimics internal engineering tooling, not a user-facing app
⚙️ How to Run Locally
1. Setup Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1

2. Install Dependencies
pip install -r requirements.txt

3. Start Server
uvicorn app.main:app --reload

4. Open Dashboard
http://127.0.0.1:8000/

🔐 Production Considerations
-Stateless API enables horizontal scaling.
-Kafka / PubSub can be added for large-scale event streaming.
-Conflict resolution logic isolated for extensibility.
-Safe for concurrent Google Sheets editors.

🏁 Conclusion

This project demonstrates:
-Real-world sync engine design.
-Safe handling of concurrent edits.
-Production-quality backend architecture.
-Clean separation of concerns.
-Built to resemble internal infrastructure tools, not demo-only code.


