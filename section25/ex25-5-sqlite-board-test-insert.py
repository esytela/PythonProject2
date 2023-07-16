'''
Ex25-5-sqlite-board-test-insert.py

'''

import sqlite3

conn = sqlite3.connect('py_board.db')
cur = conn.cursor()

# 데이터 삽입
sql = "INSERT INTO PY_BOARD " \
      "(BOARD_TITLE, BOARD_WRITER, BOARD_CONTENT) VALUES " \
      "(?, ?, ?);"
cur.execute(sql, ('test', 'dev', '테스트 중입니다.'))
conn.commit()
conn.close()


# # 데이터 조회
conn = sqlite3.connect('py_board.db')
cur = conn.cursor()
cur.close()

sql = "SELECT * FROM PY_BOARD"
cur.execute(sql)
rows = cur.fetchall()
print(rows)
cur.close()
conn.close()