# ProDev Job Board Backend

A backend system for a **Job Board Platform**, built with **Django, PostgreSQL, JWT, and Swagger**.  
The platform supports **role-based access control**, **job postings**, **applications**, and **optimized job search**.

---

## 🚀 Features
- **Job Posting Management**
  - CRUD operations for jobs.
  - Categorize jobs by **industry, location, type**.
- **Role-Based Authentication**
  - **Admins** → manage jobs and categories.
  - **Users** → apply for jobs and manage applications.
- **Optimized Job Search**
  - Indexed queries for fast filtering.
  - (Optional) Redis caching for frequently searched jobs.
- **API Documentation**
  - Interactive Swagger docs available at `/api/docs`.

---

## 🛠️ Technologies
| Technology   | Purpose                                  |
|--------------|------------------------------------------|
| Django       | Backend framework for APIs               |
| PostgreSQL   | Relational database                      |
| JWT          | Secure authentication & role management |
| Swagger      | API documentation                        |
| Redis (opt.) | Caching for faster job search            |
| Docker (opt.)| Containerization for deployment          |

---

## 📂 Project Structure
```

prodev-jobboard-backend/
│
├── jobs/               # Job postings app
├── categories/         # Job categories app
├── applications/       # Job applications app
├── users/              # User authentication & roles
├── config/             # Django project settings
│
├── requirements.txt    # Dependencies
├── docker-compose.yml  # Docker services (web, db, redis)
└── README.md           # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/prodev-jobboard-backend.git
cd prodev-jobboard-backend
````

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### 3. Configure Database

Create a PostgreSQL database and update `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jobboard',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Run migrations:

```bash
python manage.py migrate
```

### 4. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

---

## 🐳 Running with Docker (Optional)

If using Docker + Docker Compose:

```bash
docker-compose up --build
```

Services:

* `web` → Django backend (`localhost:8000`)
* `db` → PostgreSQL
* `redis` → Redis cache

---

## 🔑 API Authentication

This project uses **JWT Authentication**.

* Obtain a token by logging in:

  ```
  POST /api/token/
  ```
* Use the token in headers:

  ```
  Authorization: Bearer <your-token>
  ```

---

## 📘 API Documentation

Interactive docs available at:

```
http://localhost:8000/api/docs/
```

---

## 📊 Commit Workflow

* `feat:` → new features
* `fix:` → bug fixes
* `perf:` → performance improvements
* `docs:` → documentation updates
* `chore:` → setup/config changes

---

## 📤 Deployment

* Deploy using **Docker** or directly to **Render / Railway / Heroku**.
* Ensure environment variables are set for:

  * `SECRET_KEY`
  * `DATABASE_URL`
  * `REDIS_URL` (optional)

---

## ✅ Evaluation Criteria

1. **Functionality** → CRUD operations, role-based access, job applications.
2. **Code Quality** → Django best practices, clean schema design.
3. **Performance** → Optimized queries & indexing.
4. **Documentation** → Swagger + README clarity.

---

## 📄 License

This project is for educational purposes under the **alx's ProDev BE program**.

```

---


