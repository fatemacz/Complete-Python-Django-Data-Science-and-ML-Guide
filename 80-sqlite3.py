import sqlite3

DB_NAME = 'sqlite_db.db'

# 1. Create DB if it is absent
with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(type(sqlite_conn))


# 2. Create DB table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
        id integer PRIMARY KEY,
        title text NOT NULL,
        students_qty integer,
        reviews_qty integer
    );"""
    sqlite_conn.execute(sql_request)


# 3. Insert one record to the table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
    sqlite_conn.commit()


# 4. Write multiple records
courses = [
    (456, "JS course", 235, 50),
    (234, "Java course", 452, 20),
    (567, "Node.js course", 753, 70)
]

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()


# 5. Read records
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for course in sql_cursor:
    #     print(course)
    courses = sql_cursor.fetchall()
    print(courses)
