from tkinter import *

def clicked():
    lbl.configure(text="Да ты шутник)))")

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('500x300')
lbl = Label(window, text="Привет", font=("Arial Bold", 16))
lbl.grid(column=0, row=0)
btn = Button(window, text="От старых щеблет", font=("Arial Bold", 16), command=clicked)
btn.grid(column=1, row=0)
window.mainloop()