# 📚 LearnSphere - Backend Guide (FastAPI + SQL Server + Docker)

## ✅ Overview

**LearnSphere** is a modular, scalable backend system to manage your learning activities using FastAPI (Python), SQL Server, Redis, and MinIO—all containerized with Docker.

---

## 🚀 How to Start the Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/learnsphere-backend.git
cd learnsphere-backend
```

### 2. Create Environment Files

Create a `.env` file in each service directory (`auth_service`, `task_service`, etc.) and define required variables:

```env
DB_HOST=sql_server
DB_USER=sa
DB_PASSWORD=YourStrong@Passw0rd
DB_NAME=learnsphere
```

### 3. Build and Start Containers

```bash
docker-compose up --build
```

This command will:

* Build all FastAPI services
* Start SQL Server, Redis, and MinIO

### 4. Access Services

* Auth Service: [http://localhost:8001/docs](http://localhost:8001/docs)
* SQL Server: localhost:1433
* Redis: localhost:6379
* MinIO: [http://localhost:9000](http://localhost:9000)

---

## 🧱 Project Structure

```
learnsphere-backend/
│
├── auth_service/
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   └── auth.py
│   ├── services/
│   ├── commands/
│   └── requirements.txt
│
├── task_service/
│   └── (similar structure)
├── progress_service/
│   └── (similar structure)
├── notification_service/
│   └── (similar structure)
│
├── docker-compose.yml
└── README.md
```

---

## 🗄️ SQL Server Table Schemas (No Relationships)

### Users

```sql
CREATE TABLE Users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    email NVARCHAR(100) NOT NULL UNIQUE,
    hashed_password NVARCHAR(255) NOT NULL,
    created_at DATETIME2 DEFAULT GETDATE()
);
```

### Tasks

```sql
CREATE TABLE Tasks (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    title NVARCHAR(100) NOT NULL,
    description NVARCHAR(MAX),
    due_date DATETIME2,
    is_completed BIT DEFAULT 0,
    created_at DATETIME2 DEFAULT GETDATE()
);
```

### Progress

```sql
CREATE TABLE Progress (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    task_id INT NOT NULL,
    progress_percent INT CHECK (progress_percent BETWEEN 0 AND 100),
    last_updated DATETIME2 DEFAULT GETDATE()
);
```

### Notifications

```sql
CREATE TABLE Notifications (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT
```
