# Report Management System Backend (Django)

This is the backend of the Report Management System developed using Django. The application handles the management, creation, and retrieval of reports for users. It provides an API that allows for report generation, viewing, and management.

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
