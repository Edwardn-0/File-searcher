import os
import clipboard
import tkinter as tk
import tkinter.font

window = tk.Tk()
window.title('File searcher')
window.geometry('500x200+100+100')
filepath = ''
direct = ''

rv = tk.IntVar()

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


def btn_event():
    global filepath
    global direct 
    name = entry_file.get()
    filepath = findfile(name, direct)
    label_location.config(text = filepath)
    if filepath == None:
        label_location.config(text = '파일을 찾을 수 없습니다')

def funcC():
    global direct
    direct = 'C:/'
def funcD():
    global direct
    direct = 'D:/'

def copy():
    global filepath
    clipboard.copy(filepath)

def file_open():
    global filepath
    os.startfile(filepath)

def path_open():
    global filepath
    filepath2 = os.path.split(filepath)
    os.startfile(filepath2[0])


title_font = tkinter.font.Font(family='Consolas', size=15)

label_title = tk.Label(window, text = 'File search', width=25, height=1, relief='solid', font=title_font)
entry_file = tk.Entry(window)
btn = tk.Button(window, text = 'search', command=btn_event)
label_location_title = tk.Label(window, text = 'File location', width=15, height=2, relief='solid')
label_location = tk.Label(window, text = '<파일 위치>')
copy_btn = tk.Button(window, text='copy', command=copy)


to_C = tk.Radiobutton(window, text='C:', variable=rv, value=1, command=funcC)
to_D = tk.Radiobutton(window, text='D:', variable=rv, value=2, command=funcD)

file_start_btn = tk.Button(window, text='File Open', command=file_open)
path_start_btn = tk.Button(window, text='Path Open', command=path_open)

# label_title.grid(row=0, column=1)
# to_C.grid(row=1, column=0)
# to_D.grid(row=1, column=1)
# entry_file.grid(row=2, column=1)
# btn.grid(row=2, column=2)
# label_location_title.grid(row=3, column=1)
# label_location.grid(row=4, column=1)
# copy_btn.grid(row=4, column=2)
# file_start_btn.grid(row=5, column=1)
# path_start_btn.grid(row=6, column=1)



label_title.place(x=50,y=0)
to_C.place(x=45,y=30)
to_D.place(x=95,y=30)
entry_file.place(x=45,y=60)
btn.place(x=200,y=55)
label_location_title.place(x=50,y=90)
label_location.place(x=50,y=130)
copy_btn.place(x=250,y=160)
file_start_btn.place(x=50,y=160)
path_start_btn.place(x=150,y=160)


window.mainloop()