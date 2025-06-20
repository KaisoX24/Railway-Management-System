# 🚆 Railway Management System

A GUI-based Railway Management System built using Python and CustomTkinter. This project provides a simple and intuitive interface for users to register, log in, and manage railway ticket bookings with basic CRUD operations – book, view, and cancel tickets.

---

## 📌 Features

- ✅ User Registration and Login system with validation
- ✅ Ticket Booking with unique Ticket ID generation
- ✅ View tickets by Ticket ID or Passenger Name
- ✅ Cancel booked tickets with confirmation
- ✅ Tooltips and input validation
- ✅ Fully GUI-powered using `customtkinter`

---
## 🛠️ Tech Stack

| **Technology**       | **Purpose**                                       |
| -------------------- | ------------------------------------------------- |
| Python               | Core programming language                         |
| CustomTkinter        | Modern Tkinter GUI framework                      |
| Tkinter MessageBox   | Pop-up dialogs for user interaction               |
| UUID                 | Generate unique Ticket IDs                        |
| In-Memory Dictionary | Store ticket data during runtime (non-persistent) |

---
## 📁 Project Structure
```bash
RailwayManagementSystem/
├── main.py                # The main GUI application (your current file)
├── sql_password.py         # Stores users Mysql password
├── database_config.py      # Establizes the database connection
├── user_management.py     # Handles user registration and login
├── ticket_management.py   # Handles Ticket Management
├── README.md              # This file
```
---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KaisoX24/Railway-Management-System.git
cd Railway-Management-System
```
### 2. Install Dependencies
It's recommended to use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate # For MAC: source venv/bin/activate
```
- Install the required packages:
  ```bash
  pip install customtkinter uuid mysql-connector-python

### 3. Run the App
  ```bash
  python main.py
  ```
---
