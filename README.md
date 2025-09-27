# Job Board Backend  

A Django REST Framework backend for a job board platform with role-based authentication, efficient database queries, and Swagger API documentation.  

## 🚀 Features  
- User authentication with **roles** (`admin`, `user`)  
- Admins can **create job postings**  
- Users can **browse and filter job postings**  
- Optimized database with **indexes** for fast queries  
- API documentation with **Swagger (drf-yasg)**  

## 🛠 Tech Stack  
- **Django** + **Django REST Framework**  
- **PostgreSQL** (or MySQL if required)  
- **drf-yasg** for Swagger docs 
- **Redis** for Cache
- **JWT** for authentication 

## ⚙️ Setup  

### 1. Clone the repo  
```bash
git clone https://github.com/BeamlakF/prodev-job-platform-backend.git
cd prodev-job-platform-backend
````

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:


### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Run server

```bash
python manage.py runserver
```

## 📖 API Documentation

Once the server is running, visit:

* Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## 🔑 API Endpoints

### Authentication

* `POST /api/auth/login/` – Login with username & password
* `POST /api/auth/logout/` – Logout

### Jobs

* `GET /api/jobs/` – List all jobs (users & admins)
* `POST /api/jobs/` – Create job (admins only)
* `GET /api/jobs/{id}/` – Retrieve a job
* `PUT /api/jobs/{id}/` – Update job (admins only)
* `DELETE /api/jobs/{id}/` – Delete job (admins only)

### Users

* `GET /api/users/` – List all users (admins only)

## 📊 Database Optimization

* Indexed `title` and `company` fields in job model for faster search
* Used `select_related` and `prefetch_related` where applicable

### alx cohort 2, project nexus

### September 28, 2025

