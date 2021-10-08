from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import ttk

def clicked():
    a = "текст 1"
    b = "текст 2"
    c = "текст 3"
    def clicked1():
        lbl.configure(text=selected.get())
    selected = StringVar()
    rad1 = Radiobutton(tab1, text='Первый', value=a, variable=selected)
    rad2 = Radiobutton(tab1, text='Второй', value=b, variable=selected)
    rad3 = Radiobutton(tab1, text='Третий', value=c, variable=selected)
    btn = Button(tab1, text="Клик", command=clicked1)
    lbl = Label(tab1)
    rad1.grid(column=0, row=2)
    rad2.grid(column=0, row=3)
    rad3.grid(column=0, row=4)
    btn.grid(column=1, row=2)
    lbl.grid(column=1, row=3)

window = Tk()
window.title("SANUS TERGUM")
window.geometry('600x600+660+200')
window.resizable(True, True)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Программа')
lbl = Label(tab1, text="Привет!", font=("Bahnschrift SemiBold", 25))
lbl.grid(column=0, row=0)
lbl = Label(tab1, text="Запустить -", font=("Bahnschrift SemiBold", 25))
lbl.grid(column=0, row=1)
btn = Button(tab1, text="вжух", bg="white", fg="black", font=("Bahnschrift SemiBold", 18), command=clicked)
btn.grid(column=1, row=1)
tab_control.add(tab2, text='О проекте')
lbl = Label(tab2, text="В связи с ситуацией, возникшей в начале\n"
                       "2020 года, то есть карантином и самоизоляцией,\n"
                       "люди начали больше времени проводить дома.\n"
                       "Задачу связи с внешним миром по большей части\n"
                       "взял на себя компьютер (ПК): через него\n"
                       "проходило обучение, общение и развлечение\n"
                       "(игры, фильмы и т.п.). Меня это стороной не\n"
                       "обошло. После месяца жизни в таком виде я\n"
                       "начал чувствовать боль в спине, не критическую,\n"
                       "но все же. С того момента я поставил себе на\n"
                       "фитнес-браслет будильник, который будет\n"
                       "срабатывать каждый раз, когда я более часа\n"
                       "нахожусь в сидячем положении. Когда он\n "
                       "срабатывает, я встаю и начинаю делать 3-5\n"
                       "минутную разминку. Но ведь не у всех людей есть\n"
                       "такой гаджет, как фитнес-браслет. Это заставило\n"
                       "меня задуматься о создании программы\n"
                       "для компьютера.", font=("Bahnschrift SemiBold", 18))
lbl.grid(column=0, row=1)
tab_control.pack(expand=1, fill='both')
window.mainloop()