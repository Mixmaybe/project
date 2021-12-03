from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox

# функция кнопки Я БУДУ РАБОТАТЬ
def workmode():
    lbl = Label(tab1, text="На сколько минут выставить таймер?", font=("Bahnschrift SemiBold", 25))
    lbl.pack(anchor=N, padx=0, pady=0)
    txt = Entry(tab1, width=10)
    txt.pack(anchor=S, padx=0, pady=0)



# функция кнопки СТАРТ
def click_start():
    lbl = Label(tab1, text="Как вы будете пользоваться компьютером?", font=("Bahnschrift SemiBold", 17))
    lbl.pack(anchor=N, padx=0, pady=0)
    btn = Button(tab1, width=30, height=1, text="Я буду играть)", relief=GROOVE, bd=3, bg="light goldenrod", fg="black",
                 activebackground='RoyalBlue2', font=("Bahnschrift SemiBold", 17), command=workmode)
    btn.pack(anchor=N, padx=0, pady=0)
    btn = Button(tab1, width=30, height=1, text="Я буду работать(", relief=GROOVE, bd=3, bg="LemonChiffon3", fg="black",
                 activebackground='RoyalBlue2', font=("Bahnschrift SemiBold", 17), command=workmode)
    btn.pack(anchor=N, padx=0, pady=0)
    btn = Button(tab1, width=30, height=2, text="Я буду смотреть видео\n/слушать музыку", relief=GROOVE, bd=3, bg="light steel blue", fg="black",
                 activebackground='RoyalBlue2', font=("Bahnschrift SemiBold", 17))
    btn.pack(anchor=N, padx=0, pady=0)
    btn = Button(tab1, width=30, height=1, text="Компьютер будеть работать в фоне", relief=GROOVE, bd=3, bg="RosyBrown1", fg="black",
                 activebackground='RoyalBlue2', font=("Bahnschrift SemiBold", 17))
    btn.pack(anchor=N, padx=0, pady=0)


# САМО ОКНО
window = Tk()
window.title("SANUS TERGUM")
window.geometry('620x600+660+200')
window.resizable(False, False)
window.iconbitmap("позвоночник.ico")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# первая вкладка
tab_control.add(tab1, text='Программа')
lbl = Label(tab1, text="Добро пожаловать в программу!", font=("Bahnschrift SemiBold", 20))
lbl.pack(anchor=N, padx=0, pady=0)
btn = Button(tab1, width=10, height=1, text="СТАРТ", relief=GROOVE, bd=6, bg="white", fg="black",
             activebackground='RoyalBlue2', font=("Bahnschrift SemiBold", 18), command=click_start)
btn.pack(anchor=N, padx=0, pady=0)
# btn = Button(tab1, width=10, height=1, text="ВЫХОД", relief=GROOVE, bd=6, bg="white", fg="black", activebackground='firebrick3', font=("Bahnschrift SemiBold", 18), command=quit)
# btn.pack(anchor=S, padx=0, pady=0)

# вторая вкладка
tab_control.add(tab2, text='О проекте')

tab_control.pack(expand=1, fill='both')


window.mainloop()
