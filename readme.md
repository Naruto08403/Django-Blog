# Django Vlog Application

## Setup and Installation

1. Create and activate virtual environment (if not already done):
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Accessing the Application

- Main application: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

## Features

- View list of vlogs with pagination
- Create new vlogs with title, video URL, description, and tags
- Edit existing vlogs
- User authentication
- Admin interface for content management

Admin Access
User :Admin
Pass: Admin!23