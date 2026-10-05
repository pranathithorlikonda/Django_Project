# Institute Management System

A full-stack web application developed to simplify and manage institute operations, student records, and staff information. The system provides an efficient interface for managing data through CRUD operations.

## Features

- Student management
- Staff management
- Add, update, view, and delete records
- Centralized database management
- Responsive user interface
- Django-based backend
- Simple and user-friendly admin interface

## Technologies Used

| Layer | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap |
| Database | PostgreSQL |
| Tools | Git, GitHub, VS Code |

## Project Objective

To develop a simple and efficient system for managing student and staff records, reducing manual administrative work, and improving data accuracy through a centralized web-based platform.

## Project Structure

```text
institute-management-system/
│
├── institute_app/          # Django application
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, and images
├── requirements.txt
└── manage.py
```

## Installation

### Prerequisites

- Python 3.10 or above
- PostgreSQL
- Git

### Setup Instructions

1. Clone the repository:

```bash
git clone <your-repository-url>
cd institute-management-system
```

2. Create and activate a virtual environment:

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL:

Create a new PostgreSQL database and update the database name, username, password, host, and port in the `DATABASES` section of `settings.py`.

For better security, use environment variables instead of adding database credentials directly to the code.

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

7. Start the Django development server:

```bash
python manage.py runserver
```

8. Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## How It Works

1. The admin or authorized user logs in to the system.
2. The user can add, view, update, or delete student and staff records.
3. All records are stored securely in the PostgreSQL database.
4. The responsive interface allows easy data management from any device.

## Future Enhancements

- Add user authentication and role-based access control
- Add attendance and fee management modules
- Generate reports and export data to Excel or PDF
- Add search and filtering functionality
- Deploy the application to a cloud platform

## Author

**Pranathi Thorlikonda**

- GitHub: [pranathithorlikonda](https://github.com/pranathithorlikonda)
- LinkedIn: [Pranathi Thorlikonda](https://www.linkedin.com/in/pranathi-thorlikonda-929804376/)

