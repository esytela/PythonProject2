'''
SQLite
    오픈 소스 관계형 데이터 베이스
    서버가 필요하지 않으며, 파일 기반 데이터베이스로 동작한다.
    로컬 시스템에서 바로 사용할 수 있다
'''

import sqlite3
db_file = 'hr.db'

conn = sqlite3.connect(db_file)
cur =conn.cursor()

cur.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone_numer TEXT,
    hire_date TEXT,
    job_id TEXT,
    salary REAL,
    commission_pct REAL,
    manager_id INTEGER,
    department_id INTEGER
)
''')

cur.close()
conn.close()