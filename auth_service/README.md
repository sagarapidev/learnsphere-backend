
# Auth Service

This is an authentication service built with **FastAPI** that provides basic user management (create, read, update, delete), authentication, and security features.

## Project Structure

The project is organized into the following directories:

```
auth_service/
├── .env                # Environment variables for development
├── .gitignore          # Git ignore configuration
├── README.md           # Project documentation (this file)
├── main.py             # FastAPI application entry point
├── requirements.txt    # List of Python dependencies
└── app/
    ├── api/            # API routes and versioning
    │   └── v1/         # Version 1 of the API
    │       ├── routes/ # API route definitions
    │       │   └── users.py    # Routes for user-related actions
    │       └── routes.md       # Documentation for API endpoints
    ├── core/           # Core functionalities such as configuration and security
    │   ├── config.py   # Configuration settings for the app (e.g., DB, JWT secrets)
    │   ├── database.py # Database connection setup
    │   └── security.py # Security-related utilities (password hashing, JWT signing)
    ├── crud/           # CRUD operations on models (e.g., user)
    │   └── user.py     # User CRUD operations
    ├── deps/           # Dependency injection files (e.g., for database session)
    │   └── get_db.py   # Dependency for getting the database session
    ├── models/         # Database models
    │   └── user.py     # User model definition for the database
    ├── schemas/        # Pydantic schemas for request/response validation
    └── scripts/         # SQL scripts (e.g., database schema or data population)
        └── users.sql   # SQL script to create initial user data
```

### File Descriptions

1. **.env**:  
   This file contains environment variables like database URLs, JWT secrets, and other configuration settings that should not be hardcoded. It is ignored by Git for security reasons.

2. **.gitignore**:  
   Specifies files and directories that should not be committed to the Git repository. This typically includes environment files, virtual environments, and other temporary files.

3. **README.md**:  
   This file, which serves as the project documentation. It provides information on setting up, running, and using the authentication service.

4. **main.py**:  
   The entry point for the FastAPI application. It creates the FastAPI instance, defines middleware, and includes routes from different modules.

5. **requirements.txt**:  
   Lists the Python dependencies required for the project. These dependencies can be installed using `pip install -r requirements.txt`.

---

### `app/` Directory Breakdown

- **api/**:  
  This directory contains the API definitions. It is organized by version (`v1`) to allow for versioning of the API as the project evolves.
  
  - **v1/routes/**:  
    Contains the route files for the API. For example, `users.py` defines routes related to user management (e.g., creating users, user login).
  
  - **routes.md**:  
    Documentation detailing the API endpoints for version `v1`.

- **core/**:  
  This directory contains core functionality, such as configuration, database connection, and security utilities.

  - **config.py**:  
    Contains application configuration settings like database connection strings and JWT secrets.
  
  - **database.py**:  
    Handles the database connection logic and session management.
  
  - **security.py**:  
    Provides utilities for securely handling passwords (hashing and verification) and generating JWT tokens for authentication.

- **crud/**:  
  Contains files that define the CRUD (Create, Read, Update, Delete) operations for interacting with the database.
  
  - **user.py**:  
    Contains functions for managing users, like creating a new user, updating user details, and deleting users.

- **deps/**:  
  Defines dependencies that can be injected into API endpoints. These could be database sessions, authentication checks, etc.
  
  - **get_db.py**:  
    A function that provides a database session to be used in route handlers. It handles opening and closing the database session.

- **models/**:  
  Contains database models (using SQLAlchemy or other ORM libraries) that map to your database tables.
  
  - **user.py**:  
    Defines the `User` model, which represents a user record in the database (including fields like `username`, `email`, `password`, etc.).

- **schemas/**:  
  Contains Pydantic schemas used for validating incoming requests and serializing outgoing responses. Pydantic models help ensure that the data is in the expected format.

- **scripts/**:  
  SQL scripts to set up your database or populate it with initial data.
  
  - **users.sql**:  
    An SQL script that contains the necessary SQL commands for creating or populating the `users` table in the database.

---

## How to Run the Application

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/auth_service.git
    cd auth_service
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Create a `.env` file based on the example or template in the repository, ensuring that sensitive information (e.g., database URLs, JWT secrets) are properly set.

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

5. Access the API documentation at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

For detailed information on API routes and usage, refer to `app/api/v1/routes.md`.

- **POST /users/**: Create a new user
- **GET /users/{user_id}**: Retrieve user information by ID
- **PUT /users/{user_id}**: Update user information
- **DELETE /users/{user_id}**: Delete a user

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
