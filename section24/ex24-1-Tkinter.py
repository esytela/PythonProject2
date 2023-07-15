'''
tkinter
    Python에서 기본적으로 제공하는 GUI (Graphical User Interface)
    프로그램 모듈

    tkinter 모듈은 간단하게 GUI 프로그램 만들기 좋다
    모듈 pyQT

    작은 레이블 만듬
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack() #window에다가 글을 넣는다는 뜻

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

checkbox_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me!", variable=checkbox_var)
checkbutton.pack()

var = tk.StringVar()
var.set("option1")
radionbutton1 = tk.Radiobutton(root, text ="Option1", variable=var, value="option1")
radionbutton2 = tk.Radiobutton(root, text ="Option2", variable=var, value="option2")
radionbutton1.pack()
radionbutton2.pack()

scale = tk.Scale(root, from_=0, to=10, orient = tk.HORIZONTAL)
scale.pack()

spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

combo = ttk.Combobox(root, values=["Item 1", "Item 2", "Item 3"])
combo.pack()

def onClick():
    print("Button Click!")
    s_entry = entry.get() #변수의 값을 얻어옴
    s_text = text.get('1.0', tk.END)#END는 상수
    s_radiobutton = var.get()
    i_checkbox_var = checkbox_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()

    print(f's_entry: {s_entry}')
    print(f's_text: {s_text}')
    print(f's_radiobutton: {s_radiobutton}')
    print(f's_checkbox_var: {i_checkbox_var}')
    print(f'i_scale: {i_scale}')
    print(f'i_spinbox: {i_spinbox}')
    print(f's_combo: {s_combo}')


button = tk.Button(root, text='click me!', command=onClick)
button.pack()

#실행코드
root.mainloop()