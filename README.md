# movie-catalog API

Built a fully featured movie catalog API with JWT authentication, role-based permissions and staff-restricted CRUD operations. implemented pagination, 
advanced filtering (genre, rating, director etc.) search, ordering, rate limiting and API versioning for scalable performance.

---

## Features

- **User Auth**  
User registration and login are implemented using JSON Web Tokens (JWT) via Simple JWT, with full support for token refresh and rotation to ensure secure and seamless authentication.

- **Movies CRUD**  
  - **Create** only if you’re a staff member. 
  - **Read** (list/detail) Everyone.
  - **Update** or **Partial Update** only if you’re a staff member.  
  - **Delete** only if you’re a staff member.

- **API Niceties**  
  - **Pagination**: Flexible and configurable page sizes to suit varying client needs.  
  - **Filter** & **Search**: Query the movies by genre, rating, actors, movie names etc.  
  - **Ordering**: Allows clients to sort movie results by specified fields, such as rating to display movies in a desired order.
  - **Throttling**: Prevents from hammering the API.  
  - **Versioning**: backward-incompatible changes require clear and structured communication.

---

## Tech Stack

- **Python 3.x**  
- **Django 4.x**  
- **Django REST Framework**  
- **djangorestframework-simplejwt**  
- **SQLite** 
- **django-filter**  

---

## Installation

1. **Clone it**  
   ```bash
   git clone https://github.com/aref0101/Movie-API.git
   cd Movie-API

# 2. Create & activate a virtualenv
python -m venv .venv

source .venv/bin/activate      # macOS/Linux

.venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
SECRET_KEY=your-django-secret-key-avoid-using-‘django-insecure’

DEBUG=True   # switch to False in prod

ALLOWED_HOSTS=127.0.0.1, localhost

# 5. python manage.py migrate
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. start the project
python manage.py runserver
>>>>>>> b47550f (initial commit)
