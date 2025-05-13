# 🧠 Task Service - FastAPI + SQL Server

A backend microservice for managing tasks, built with **FastAPI** and **SQL Server**, following clean architecture and production-ready standards.

---

## 🗂️ Project Structure

```
task-service/
├── app/
│   ├── controller/         # API route handlers
│   ├── service/            # Business logic (interfaces + implementations)
│   ├── model/              # SQLAlchemy models
│   ├── schema/             # Pydantic schemas (for request/response)
│   ├── repository/         # (Optional) For future DB abstraction
│   ├── config/             # DB setup and env loading
│   └── main.py             # App entry point
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/task-service.git
cd task-service
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Update your `.env` file with your **MSSQL** credentials:

```env
DATABASE_URL=mssql+pyodbc://sagar:p%40%24%24word@localhost:1433/Java_MSA?driver=ODBC+Driver+17+for+SQL+Server
```

> Tip: Use URL encoding for special characters in the password.

---

## 🚀 Run the Application

```bash
uvicorn app.main:app --reload
```

- The API will be available at: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

---

## 📬 API Endpoints

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | `/tasks/`      | Get all tasks       |
| POST   | `/tasks/`      | Create a new task   |

---

## 🛠 Tech Stack

- **FastAPI** – Web Framework
- **SQLAlchemy** – ORM
- **PyODBC** – SQL Server Driver
- **Pydantic** – Data validation
- **Uvicorn** – ASGI Server

---

## ✅ Features

- Production-grade project structure
- MSSQL integration via SQLAlchemy
- Clean separation of concerns
- Easily extensible for auth, logging, and more

---

## 📦 Future Enhancements

- ✅ JWT Authentication
- ✅ Unit tests with Pytest
- ✅ Alembic DB migrations
- ✅ Pagination, filtering
- ✅ Logging and monitoring

---

## 🤝 Contributing

Feel free to fork the project and submit pull requests. Contributions are welcome!

---

## 📝 License

MIT License
