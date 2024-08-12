# Gérer-les-authentifications-dans-django
# Django Authentication Project

This is a simple Django project demonstrating a basic user authentication system. It includes user signup, login, logout, and displaying the username of the logged-in user on the homepage.

## Features

- User registration with validation
- User login and logout functionality
- Display logged-in user's name on the homepage
- Redirection to the homepage upon logout

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- A virtual environment tool (optional but recommended)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mikelebake/gerer-les-authentifications-dans-django.git
   cd gerer-les-authentifications-dans-django
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Navigate to the project directory:**

   Make sure you are in the directory containing `manage.py`.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   Open your browser and go to `http://127.0.0.1:8000/` to see the homepage.

## Usage

- **Sign Up:** Navigate to `/signup/` to create a new user account.
- **Log In:** Navigate to `/login/` to log in with an existing account.
- **Log Out:** Click the logout button on the homepage to log out and be redirected to the homepage.

## Project Structure

```
myproject/
├── accounts/
│   ├── templates/
|   |   |── home.html
│   │   ├── accounts/
│   │   │   ├── signup.html
│   │   ├── registration/
│   │   │   ├── login.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Contact

For questions or suggestions, please open an issue or contact me at [your-email@example.com](mailto:emaick9@gmail.com).


