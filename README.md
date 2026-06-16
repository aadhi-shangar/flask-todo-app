# TaskFlow - Flask Todo Application

A modern Todo Management web application built with Flask, SQLAlchemy, and SQLite. TaskFlow helps users organize tasks efficiently with authentication, task tracking, and a clean responsive interface.

## Features

* User Registration and Login
* Session-Based Authentication
* Create New Tasks
* Edit Existing Tasks
* Delete Tasks
* Mark Tasks as Completed or Pending
* Task Statistics Dashboard
* Responsive UI Design
* SQLite Database Integration

## Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy
* SQLite

### Frontend

* HTML5
* CSS3
* Jinja2 Templates
* Font Awesome

## Project Structure

```text
task-manager-flask/
│
├── auth.py
├── main.py
├── models.py
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── todo_form.html
│
└── instance/
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/aadhi-shangar/flask-todo-app.git
cd flask-todo-app
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask flask-sqlalchemy
```

### Run the Application

```bash
python main.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Screenshots

Add screenshots of:

* Login Page
* Registration Page
* Dashboard
* Create Task Page

## Future Improvements

* Password Hashing
* Task Categories
* Task Priorities
* Search and Filtering
* Due Date Notifications
* REST API Support
* Docker Deployment

## Learning Outcomes

This project demonstrates:

* Flask Routing
* User Authentication
* SQLAlchemy ORM
* CRUD Operations
* Session Management
* Template Rendering with Jinja2
* Responsive UI Design

## Author

**Aadhishangar**

GitHub: https://github.com/aadhi-shangar

## License

This project is licensed under the MIT License.
