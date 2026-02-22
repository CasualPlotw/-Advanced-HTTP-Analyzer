# Advanced HTTP Analyzer 🚀

A multi-threaded HTTP analyzer built using raw Python sockets.

This project demonstrates low-level HTTP request handling, logging, and basic route management without using any external web frameworks.

---

## 🔥 Features

- Multi-threaded client handling
- Raw HTTP request parsing
- JSON-based request logging
- Path statistics tracking
- 403 Forbidden route blocking
- Live server stats endpoint
- Log export endpoint

---

## 📦 Endpoints

| Endpoint | Description |
|----------|------------|
| `/` | Default welcome page |
| `/stats` | Shows total request count and path statistics |
| `/logs` | Returns all logs in JSON format |
| `/admin` | Blocked route (returns 403 Forbidden) |

---

## 🛠 Technologies Used

- Python
- socket
- threading
- datetime
- json

---

## ▶️ How to Run

```bash
python analyzer_server.py
```

Server runs on:

http://127.0.0.1:8080

---

## 📊 Example Log Entry

```json
{
  "time": "2026-02-22 09:07:18.340123",
  "ip": "127.0.0.1",
  "method": "GET",
  "path": "/stats"
}
