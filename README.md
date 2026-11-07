# Assignment 3: Database Interaction with PostgreSQL and Application Programming

This application creates a connection to a PostgreSQL database and performs CRUD operations on a `students` table using [psycopg 3](https://www.psycopg.org/psycopg3/).

**Video demonstration:** [link here](https://example.com)

## Repository Structure

```
a3/
├── app/
│   └── main.py          # app code: db connection and CRUD functions (get, insert, update, delete)
├── db/
│   ├── create_db.sql    # creates the a3_db database
│   └── setup.sql        # creates the students table and inserts the initial data
├── .env.example         # template for database credentials
├── requirements.txt     # Python dependencies
└── README.md
```

## Application Functions

| Function | Description |
|---|---|
| `getAllStudents()` | Gets and prints all records from the `students` table |
| `addStudent(first_name, last_name, email, enrollment_date)` | Inserts a new student record |
| `updateStudentEmail(student_id, new_email)` | Updates the email of the student with the matching ID |
| `deleteStudent(student_id)` | Deletes the student with the matching ID |

## Prerequisites

- Python 3.10+
- A running PostgreSQL server
- pgAdmin (or `psql`) to run the SQL scripts

## Setup

### 1. Create the database and table

In pgAdmin:

1. Right-click the default `postgres` database and open a Query Tool. Then run the code inside `db/create_db.sql`. This will create `a3_db`.
2. Right-click Databases and press Refresh. Then open a Query Tool on `a3_db`, and run the code inside `db/setup.sql`. This will create the `students` table and insert the three records from the initial data.

`setup.sql` will drop and create the table again, so it can be executed again to reset the data.

### 2. Set up the Python environment

From the repository root:

```bash
python -m venv venv

# Windows (PowerShell); what I'm using
.\venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure database credentials

Copy `.env.example` to `.env` and fill in your PostgreSQL details:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=a3_db
DB_USER=postgres
DB_PASSWORD=your_password
```

`.env` is listed in `.gitignore`, so the db credentials are never committed.

> **Note:** If PostgreSQL runs on a remote VM that only listens on localhost (like in my setup), open an SSH tunnel first and keep it open while running the app:
> ```bash
> ssh -L 5432:localhost:5432 <user>@<vm-ip>
> ```

## Running the Application

```bash
python app/main.py
```

By default, `main()` calls `getAllStudents()`. The calls to the other functions are commented out in `main()`. Uncomment them one at a time to run each operation, then check the result in pgAdmin with:

```sql
SELECT * FROM students ORDER BY student_id;
```