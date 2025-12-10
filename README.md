***Task Manager API (Django)***
A simple Django REST API for managing tasks with JWT authentication and role-based access (Admin/User).
Users can create and manage their own tasks, while admins can view all tasks.

***Features***
1. User registration
2. Login using JWT
3. Create, view, update and delete tasks
4. Users see only their own tasks
5. Admin can see every user's tasks

***How to run***
1. Create a virtual environment and install requirement:
   pip freeze > requirements.txt  or pip install -r requirements.txt
2. Apply migrations:
   python manage.py migrate
3. Start the server:
   python manage.py runserver

***API Endpoints***

Auth:
1. POST/auth/register
2. POST/auth/login
   
Tasks (JWT required):
1. GET/tasks/
2. POST/tasks/
3. GET/tasks/<id>/
4. PUT/tasks/<id>/
5. DELETE/tasks/<id>/
   
Roles:
1. Admin: can view and manage all tasks
2. User: can only access their own tasks
   
Tech Stack:
1. Django
2. Django REST Framework
3. SimpleJWT
4. SQLite

Important:
1. Tested using Postman
2. Groups (Admin/User) are used to control permissions
    
