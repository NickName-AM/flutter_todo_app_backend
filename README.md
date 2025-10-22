# Django REST Framework Backend

This is a backend REST API built using **Django** and **Django REST Framework (DRF)** for the **[flutter_todo_app](https://github.com/NickName-AM/flutter_todo_app)**.  
It provides secure, efficient, and scalable APIs for authentication and data management.

---

## Tech Stack

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Django Simple JWT** – for authentication
- **SQLite** – as the database (configurable)

---

## Features

- User Authentication (Register, Login)
- CRUD operations for core models
- Token-based Authentication (JWT)
- Clean, modular code structure (apps separated)
- CORS-enabled for frontend integration
- Admin panel for data management

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/NickName-AM/flutter_todo_app.git
cd flutter_todo_app
```

### 2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server
```
python manage.py runserver 0.0.0.0:8000
```