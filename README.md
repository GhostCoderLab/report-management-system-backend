# Django Development Environment

A development environment for Django projects. This project includes basic Django configurations, dependencies, database setup, and testing preparations.

---

## 📂 Project Structure

```plaintext
Django Development Environment
├── README.md
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __pycache__
│   │   ├── base.py
│   │   └── development.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.lock
└── requirements.txt
```

## 🛠️ Installation Instructions
1. Clone the repository
2. If the `api` files are not needed, you can delete them.
3. Start the development server
```bash
python manage.py runserver --settings config.settings.development
```
