1.curl -sSL https://install.python-poetry.org | python3 - or pipx install poetry # if you use pipx
2.C:\Users\sagar\development\PYTHON-PRG\learnsphere-backend\poetry-app>poetry init 3. Directory of C:\Users\sagar\development\PYTHON-PRG\learnsphere-backend\poetry-app

17-05-2025 02:34 <DIR> .
17-05-2025 02:33 <DIR> ..
17-05-2025 02:34 412 pyproject.toml
1 File(s) 412 bytes
2 Dir(s) 860,211,232,768 bytes free
  
fresh project:
step1:
task-api-service/
├── app/
│ ├── main.py
│ ├── core/
│ │ └── config.py
│ └── infrastructure/
│ └── database/
│ ├── connection.py
│ └── models/
│ └── user.py
├── .env
├── pyproject.toml

step 2: poetry init --name task-api-service --dependency fastapi --dependency uvicorn --dependency sqlalchemy --dependency python-dotenv --dependency pyodbc
step 3: pyproject.toml
step4: poetry install
step5: poetry run uvicorn main:app --reload
