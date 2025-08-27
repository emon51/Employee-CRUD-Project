# Employee Management System

This is a Employee Management System built with Django. It allows to manage employees, departments and achievements with proper user authentication system (register, login, logout).
 
## Features
- User Registration (using email & password)
- User Login / Logout
- Manage Departments (Add, View, Update, Delete)
- Manage Acheivements (Add, View, Update, Delete)
- Manage Employees (Add, View, Update, Delete)
 
## Security
  - Proper user authentication is implemented.



## Used Technologies

- Language: Python
- Backend: Django
- Frontend: HTML
- Database: Sqlite3

# Installation & Setup

## Clone this project
   ```
    git clone https://github.com/emon51/Employee-CRUD-Project.git
   ```

## Create a virtual environment
```
python -m venv myenv
```

## Activate virtual environment (For Windows)
```
"myenv\Scripts\activate"
```

## Change the directory
```
cd Employee-CRUD-Project
```

## Install dependencies
```
pip install -r requirements.txt
```

## Migrate database
```
python manage.py migrate

```

## Run the development server
```
python manage.py runserver

```

## Open in browser
```
http://127.0.0.1:8000/

```




