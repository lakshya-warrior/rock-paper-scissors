import random
from tkinter import *

success = []


def show_image(button_press, reset):
    global success

    score_label[0].pack_forget()
    score_label[1].pack_forget()
    score_label[2].pack_forget()

    image_label[2].place_forget()
    image_label[0].place_forget()
    image_label[1].place_forget()

    image_label[3].place_forget()
    image_label[5].place_forget()
    image_label[4].place_forget()

    x_comp = screen_width / 2 - 520
    x_user = screen_width / 2 + 200

    if reset == "reset":
        success = []

        image_label[2].place_forget()
        image_label[0].place_forget()
        image_label[1].place_forget()

        image_label[3].place_forget()
        image_label[5].place_forget()
        image_label[4].place_forget()

        comp_option = "blank"
    if reset != "reset":
        comp_option = random.choice(option_list)

    if comp_option == "paper":
        image_label[4].place(x=x_comp, y=screen_width / 6)
    if comp_option == "rock":
        image_label[5].place(x=x_comp, y=screen_width / 6)
    if comp_option == "scissors":
        image_label[3].place(x=x_comp, y=screen_width / 6)

    if button_press == "paper":
        image_label[1].place(x=x_user, y=screen_width / 6)
    if button_press == "rock":
        image_label[2].place(x=x_user, y=screen_width / 6)
    if button_press == "scissors":
        image_label[0].place(x=x_user, y=screen_width / 6)

    if comp_option == button_press:
        score_label[0].pack(pady=6)
        success.append("tie")
    if comp_option == "paper" and button_press == "rock" \
            or comp_option == "rock" and button_press == "scissors" \
            or comp_option == "scissors" and button_press == "paper":
        score_label[1].pack(pady=6)
        success.append("loss")
    if comp_option == "scissors" and button_press == "rock" \
            or comp_option == "rock" and button_press == "paper" \
            or comp_option == "paper" and button_press == "scissors":
        score_label[2].pack(pady=6)
        success.append("wins")

    count = Label(screen, text="Wins = " + str(success.count("wins")).zfill(3) + "\nLoss = " +
                               str(success.count("loss")).zfill(3) +
                               "\nTies = " + str(success.count("tie")).zfill(3) +
                               "\nTotal = " + str(len(success)).zfill(4),
                  font=('Times New Roman', 15), fg='green',
                  background="#ADD8E6")
    count.place(x=1397, y=20)


def draw_screen(window, w_width, w_height):
    window.title("Rock Paper Scissors")
    window.geometry(f'{w_width}x{w_height}')
    window.configure(background="#ADD8E6")
    t1 = Label(window, text='Rock Paper Scissors', font=('Times New Roman', 45), fg='#00008B', background="#ADD8E6")
    t1.pack()

    you_label = Label(window, text='You', font=('Times New Roman', 45), fg='#FFFDD0', background="#ADD8E6")
    you_label.place(x=w_width / 2 + 270, y=110)

    line_label = Label(window, relief="solid", borderwidth=10, height=29)
    line_label.pack(pady=30)

    comp_label = Label(window, text='Computer', font=('Times New Roman', 45), fg='#FFFDD0', background="#ADD8E6")
    comp_label.place(x=w_width / 2 - 500, y=110)

    x_btn = w_width / 2 - 83

    r_btn = Button(screen, text="Rock", font=('Times New Roman', 15), fg='#FFD700', bg='#4169E1', width=15, height=2,
                   command=lambda: show_image("rock", ""))
    r_btn.place(x=x_btn - 300, y=w_height - 200)

    p_btn = Button(screen, text="Paper", font=('Times New Roman', 15), fg='#FFD700', bg='#4169E1', width=15,
                   height=2, command=lambda: show_image("paper", ""))
    p_btn.place(x=x_btn, y=w_height - 200)

    s_btn = Button(screen, text="Scissors", font=('Times New Roman', 15), fg='#FFD700', bg='#4169E1', width=15,
                   height=2, command=lambda: show_image("scissors", ""))
    s_btn.place(x=x_btn + 300, y=w_height - 200)

    reset = Button(screen, text="Reset", font=('Times New Roman', 15), fg='#FFD700',
                   bg='#4169E1', command=lambda: show_image("", "reset"))
    reset.place(x=1410, y=115)


option_list = ["rock", "paper", "scissors"]

screen = Tk()

screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
draw_screen(screen, screen_width, screen_height)

r_image = PhotoImage(file='rock.png')
p_image = PhotoImage(file='paper.png')
s_image = PhotoImage(file='scissors.png')

image_label = []
score_label = []

image_list = [s_image, p_image, r_image, s_image, p_image, r_image]
score_text_list = ["TIE!", "You LOST!", "You WON!"]
# Images
for i in range(0, 6):
    image_label.append(Label(screen, image=image_list[i], relief="flat", bg="#ADD8E6"))

# Comments
for i in range(0, 3):
    score_label.append(Label(screen, text=score_text_list[i], font=('Times New Roman', 30), fg='green',
                             background="#ADD8E6"))

screen.mainloop()
