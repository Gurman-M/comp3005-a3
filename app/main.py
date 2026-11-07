import os
import psycopg
from dotenv import load_dotenv

# reads .env into the environment variables
load_dotenv()

def get_connection():
    """Open a connection to the database using credentials from .env"""
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def getAllStudents():
    """Retrieve and display all records from the students table."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record into the students table."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) "
            "VALUES (%s, %s, %s, %s) RETURNING student_id;",
            (first_name, last_name, email, enrollment_date),
        )
        new_id = cur.fetchone()[0]

    # insert is now committed to db
    print(f"Added student {new_id}")
    return new_id

def updateStudentEmail(student_id, new_email):
    """Update the email address of the student with the given student_id."""
    update = """
    UPDATE students
    SET email = %s
    WHERE student_id = %s;
    """
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(update, (new_email, student_id))
        # number of rows matched
        updated = cur.rowcount

    if updated:
        print(f"Updated email for student {student_id}")
    else:
        print(f"No student with id {student_id}")
    return updated

def deleteStudent(student_id):
    """Delete the record of the student with the given student_id."""
    delete = """
    DELETE FROM students
    WHERE student_id = %s;
    """
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(delete, (student_id,))
        deleted = cur.rowcount

    if deleted:
        print(f"Deleted student {student_id}")
    else:
        print(f"No student with id {student_id}")
    return deleted

def main():
    getAllStudents()
    # addStudent("Cassius", "Bellona", "cassiusbellona@cmail.carleton.ca", "2026-11-07")
    # updateStudentEmail(4, "newemail@cmail.carleton.ca")
    # deleteStudent(2)
    
    # error testing: student with ID 5 does not exist!
    # updateStudentEmail(5, "newemail@cmail.carleton.ca")
    # deleteStudent(5)

if __name__ == "__main__":
    main()