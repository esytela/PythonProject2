'''
파일명: Ex25-3-sqlite-board-ddl.py
'''
import sqlite3

conn = sqlite3.connect('py_board.db')
cur = conn.cursor()

# 테이블 생성
cur.execute('''
    CREATE TABLE PY_BOARD (
        BOARD_ID INTEGER PRIMARY KEY,
        BOARD_TITLE TEXT DEFAULT NULL,
        BOARD_WRITER TEXT DEFAULT NULL,
        BOARD_CONTENT TEXT,
        BOARD_DATE DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
    )
''')

cur.close()
conn.close()