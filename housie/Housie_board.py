# Lakshya Gupta - Housie Board

from tkinter import *
import math
import random
import tkinter.font as tkFont
import pyttsx3

screen = Tk()
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
screen.title("Housie Board")
screen.geometry(f'{screen_width}x{screen_height}')
screen.configure(background="#ADD8E6")

all_num = (random.sample((range(0, 90)), 90))


def callback(event):
    gen()

def gen():
    curr_num = all_num[0] + 1

    display_num = Label(screen, text=str(curr_num).zfill(2), font=('Arial', 25), fg='red', bg="#ADD8E6")
    display_num.place(x=500, y=117)
    display_num_font = tkFont.Font(family="Arial", size=25, weight="bold", slant="italic")
    display_num.configure(font=display_num_font)

    btn[all_num[0]]["bg"] = "#C0C0C0"
    btn[all_num[0]]["fg"] = "#CC5500"

    engine = pyttsx3.init()\
    ''' For voice'''
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 140)
    engine.say("The next number is" + str(curr_num))
    engine.runAndWait()

    all_num.pop(0)
    if len(all_num) == 0:
        game_over = Label(screen, text=str("GAME OVER"), font=('Arial', 50), fg='green', bg="#ADD8E6")
        game_over.place(relx=0.5, rely=0.82, anchor='center')


x = math.ceil((screen_width - 100) / 16)
y = math.floor(screen_height / 28)
vertical_gutter = 190
btn = []
for i in range(0, 90):
    col = i % 10
    row = math.floor(i / 10)
    dis = str(i + 1)
    btn.append(Button(screen, text=dis, font=('Arial', 15), fg='black', background="white", width=int(x / 10)))
    btn[i].place(x=x + col * (x + x / 2), y=vertical_gutter + row * (y + y / 2))
t1 = Label(screen, text='Housie Board', font=('Arial', 45), fg='red', background="#ADD8E6")
t1.pack()

t2 = Label(screen, text=str("Current Number is"), fg='black', background="#ADD8E6")
t2.place(x=250, y=120)

fontExample = tkFont.Font(family="Arial", size=20, weight="bold", slant="italic")
t2.configure(font=fontExample)

button1 = Button(screen, text="Next Number", font=('Arial', 15), fg='black', background="#ADD8E6",
                 activebackground="#ADD8E6", relief=GROOVE, command=gen)
button1.bind("<Return>", callback)
button1.place(x=1200, y=120)

screen.bind('<Return>', callback)

screen.mainloop()
