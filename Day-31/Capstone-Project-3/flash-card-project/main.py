from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "COMIC SANS MS"
current_card = {}

# --------------------------------------- FETCH DATA FROM CSV ---------------------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)


# --------------------------------------- FETCH NEW CARDS -------------------------------------------- #
def new_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_background, image=card_front_image)


# --------------------------------------- FLIP THE CARD ---------------------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# --------------------------------------- UI SETUP --------------------------------------------------- #
# Creating a tkinter window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.after(4000, func=flip_card)
# Canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Fetch image and create buttons
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=new_card)
unknown_button.grid(row=1, column=0)

tick_image = PhotoImage(file="./images/right.png")
known_button = Button(image=tick_image, highlightthickness=0, bd=0, command=new_card)
known_button.grid(row=1, column=1)

new_card()

window.mainloop()
