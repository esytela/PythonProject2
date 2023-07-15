import tkinter as tk
from tkinter import ttk

class TreeViewApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('하위 아이템 추가')

        self.treeview = ttk.Treeview(self, columns=('name', 'age'))
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('name', text='이름')
        self.treeview.heading('age', text='나이')
        self.treeview.pack()

        self.add_parent_item('1', 'John', '30')
        self.add_child_item('1', '2', 'Alice', '25')
        self.add_child_item('1', '3', 'Bob', '35')

    def add_parent_item(self, id, name, age):
        self.treeview.insert('', 'end', id, text=id, values=(name, age)) #id 값이 없기에 '' 빈공간 입력 및 부모값이 됨

    def add_child_item(self, parent_id, id, name, age):
        self.treeview.insert(parent_id, 'end', id, text=id, values=(name, age))

#실행코드
app = TreeViewApp()
app.mainloop()
