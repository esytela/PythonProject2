'''
CRUD (Create, Read, Update, Delete)
'''

import sqlite3

conn = sqlite3.connect('hr.db')
cur = conn.cursor()

# 데이터 삽입
sql = "INSERT INTO employees"\
    "(first_name, last_name, email, "\
    "hire_date, job_id, salary, department_id)"\
    "VALUES (?, ?, ?, ?, ?, ?, ?)"
cur.execute(sql, ('John,', 'Doe', 'johndoe1@example,com',
                  '2023-07-15', 'IT_PROG', 5000, 90)) # values의 물읍표에 들어감

conn.commit()
cur.close()
conn.close()


# #데이터조회
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "SELECT * FROM employees WHERE employee_id = ?"
cur.execute(sql, (1,))
rows = cur.fetchall()
print(rows)


#데이터 수정
conn = sqlite3.connect('hr.db')
cur = conn.cursor()
sql = "UPDATE employees SET salary = ? WHERE employee_id = ?"
cur.execute(sql, (5500, 1)) # 1번 사원의 데이터만 바꾼다는 뜻
conn.commit()

cur.close()
conn.close()

#데이터조회
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "SELECT * FROM employees WHERE employee_id = ?"
cur.execute(sql, (1,))
rows = cur.fetchall()
print(rows)


#데이터 삭제
conn = sqlite3.connect('hr.db')
cur = conn.cursor()
sql = "DELETE FROM employees"
cur.execute(sql)
conn.commit()

cur.close()
conn.close()

print('====delete 후=====')

#데이터조회
conn = sqlite3.connect('hr.db')
cur = conn.cursor()

sql = "SELECT * FROM employees"
cur.execute(sql)
rows = cur.fetchall()
print(rows)
