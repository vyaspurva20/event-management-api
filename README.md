# Event Management API (Django REST Framework)

## Overview
This project implements an Event Management System using Django and Django REST Framework (DRF).  
It allows users to create events, RSVP to events, and leave reviews. The system uses JWT Authentication for secure access.

---

## Features
- User Profiles extending Django User
- Create, Update, Delete Events (Organizer only)
- RSVP to events (Going, Maybe, Not Going)
- Event Reviews with ratings
- Private/Public events with permissions
- Pagination + Filtering + Search
- JWT Authentication
- Optional: Celery task for email notifications
- Optional: Unit Tests using Django Test Framework

---

## Project Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/event-management-api.git
cd event-management-api
```

### 2. Create Virtual Environment
```bash
python -m venv env
env\Scripts\activate   # Windows
source env/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Server runs at:  
http://127.0.0.1:8000/

---

## API Authentication

### Get Access Token
**POST**
```
/api/token/
```

Body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Refresh Token
**POST**
```
/api/token/refresh/
```

---

## API Endpoints

### Event API
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/events/` | Create event |
| GET | `/events/` | List public events (paginated) |
| GET | `/events/{id}/` | Event details |
| PUT | `/events/{id}/` | Update event (organizer only) |
| DELETE | `/events/{id}/` | Delete event (organizer only) |

### RSVP API
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/events/{event_id}/rsvp/` | Add RSVP |
| PATCH | `/events/{event_id}/rsvp/{user_id}/` | Update RSVP |

### Review API
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/events/{event_id}/reviews/` | Add review |
| GET | `/events/{event_id}/reviews/` | List event reviews |

---

## Tech Stack
- Python 3.x  
- Django 4/5/6  
- Django REST Framework  
- SimpleJWT  
- SQLite / PostgreSQL  
- Optional: Celery + Redis

---

## How to Run Tests
```bash
python manage.py test
```

---

## Folder Structure
```
event_management/
│
├── config/
├── events/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   ├── tests.py
│
├── manage.py
├── README.md
├── requirements.txt
```

---

## Author
Your Name  
GitHub: https://github.com/<your-username>

---

## License
MIT License
