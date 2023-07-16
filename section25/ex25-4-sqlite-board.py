'''
테스트 SQL
INSERT INTO PY_BOARD (BOARD_TITLE, BOARD_WRITER, BOARD_CONTENT)
VALUES ('TEST', 'dev', '데이터 검색 테스트 중입니다.');

'''

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
import sqlite3

class BoardApp(tk.Tk):
    def __init__(self): #생성자
        super().__init__()

        self.title('게시판')

        # control 변수 선언
        self.combobox_search = ttk.Combobox(self)
        self.textfield_search = tk.Entry(self)
        self.button_search = tk.Button(self, text='검색', command=self.onclick_search)
        self.button_insert = tk.Button(self, text='신규', command=self.onclick_insert)
        self.button_delete = tk.Button(self, text='삭제', command=self.onclick_delete)
        self.button_update = tk.Button(self, text='수정', command=self.onclick_update)
        self.treeview_boardlist = ttk.Treeview(self,
                                               columns = ('id','title','writer','date'),
                                               show='headings')

        #control 배치
        self.combobox_search.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        #nsew = north south east west으로 공간 채운다는 뜻
        self.textfield_search.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        self.button_search.grid(row=0, column=2, padx=5, pady=5, sticky='ns')
        self.treeview_boardlist.grid(row=1, column=0, rowspan=3, columnspan=2,
                                     padx=5, pady=5, sticky='nsew')
        self.button_insert.grid(row=1, column=2, padx=5, pady=5, sticky='ns')
        self.button_update.grid(row=2, column=2, padx=5, pady=5, sticky='ns')
        self.button_delete.grid(row=3, column=2, padx=5, pady=5, sticky='ns')

        # 트리뷰 컬럼 설정
        self.treeview_boardlist.heading('id', text='ID')
        self.treeview_boardlist.column('id', width=50)
        self.treeview_boardlist.heading('title', text='제목')
        self.treeview_boardlist.column('title', width=300)
        self.treeview_boardlist.heading('writer', text='작성자')
        self.treeview_boardlist.column('writer', width=100)
        self.treeview_boardlist.heading('date', text='작성일')
        self.treeview_boardlist.column('date', width=150)

        # 검색 기준 설정
        self.combobox_search['values'] = ('제목','작성자')
        self.combobox_search.current(0)

    # 게시팜 초기화
    def init_boardlist(self):
        print('게시판 초기화')

        # py_board 데이터 불러오기
        rows = self.get_boardlist()

        # 트리뷰 초기화 (요소들 하나 하나 가져와서 지우겠다는 뜻)
        self.treeview_boardlist.delete(*self.treeview_boardlist.get_children())
        self.treeview_boardlist.bind('<Double-Button-1>', self.onclick_view)

        # 게시글 목록 출력
        for row in rows:
            self.treeview_boardlist.insert('', 'end', text='', values=row)

    def get_boardlist(self, keyword='', search_option=''):
        conn = sqlite3.connect('py_board.db')
        curs = conn.cursor()

        #검색 조건에 따른 WHERE 절 구성
        if search_option == '작성자' and keyword != '':
            where_clause = 'WHERE BOARD_WRITER = :1'
        else:
            where_clause = "WHERE BOARD_TITLE LIKE '%'|| :1 || '%'"

        #SQL 문 작성
        sql = f"SELECT BOARD_ID, BOARD_TITLE, BOARD_WRITER, BOARD_DATE " \
              f"FROM PY_BOARD " \
              f"{where_clause} ORDER BY BOARD_ID DESC"

        curs.execute(sql, (keyword,))

        rows = curs.fetchall()

        # 데이터베이스 연결 헤제
        curs.close()
        conn.close()

        return rows


    def onclick_search(self):
        print('검색!')

        keyword = self.textfield_search.get()

        search_option = self.combobox_search.get()

        # py_board 데이터 불러오기
        rows = self.get_boardlist(keyword, search_option)

        # 트리뷰 초기화 (요소들 하나 하나 가져와서 지우겠다는 뜻)
        self.treeview_boardlist.delete(*self.treeview_boardlist.get_children())
        self.treeview_boardlist.bind('<Double-Button-1>', self.onclick_view)

        # 게시글 목록 출력
        for row in rows:
            self.treeview_boardlist.insert('', 'end', text='', values=row)


    def onclick_insert(self):
        print('신규')

    def onclick_update(self):
        print('수정')

    def onclick_delete(self):
        print('삭제')

    def onclick_view(self):
        print('상세보기')

        selection = self.treeview_boardlist.selection()
        if not selection:
            return
        board_id= self.treeview_boardlist.item(selection, 'values')[0]

        row = self.get_board(board_id)

        view_dialog = BoardViewDialog(self, row)
        self.wait_window(view_dialog)

class BoardViewDialog(tk.Toplevel): #top Level = 새창 띄우는 것
    def __init__(self, parent, row):
        super().__init__(parent)
        self.title('게시글 보기')

        # 컨트롤 변수 선언
        self.label_title = tk.Label(self, text=row[1], font=('Arial', 14, 'bold'))
        self.label_writer = tk.Label(self, text=row[2], font=('Arial', 12))
        self.textarea_content = scrolledtext.ScrolledText(self)
        self.button_close = tk.Button(self, text='닫기', command=self.destroy)

        # 컨트롤 배치
        self.label_title.pack(side=tk.TOP, padx=5, pady=5)
        self.label_writer.pack(side=tk.TOP, padx=5, pady=5)
        self.textarea_content.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.button_close.pack(side=tk.RIGHT, padx=5, pady=5)

        self.geometry('+%d+%d' % (parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_width() / 2,
                                  parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_height() / 2,
                                  ))


# 실행코드
if __name__ == '__main__':
   app = BoardApp()
   app.mainloop()
