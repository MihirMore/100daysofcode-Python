from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "COMIC SANS MS"


# --------------------------------------- PASSWORD GENERATOR ----------------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# --------------------------------------- SAVE PASSWORD ---------------------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered: \nEmail: {email} \nPassword: "
                                               f"{password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------------------- UI SETUP --------------------------------------------------- #
# Creating a tkinter window
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=60)
# creating a Canvas to add out image
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# Creating labels to add text on screen
website_label = Label(text="Website :", font=(FONT_NAME, 12, "normal"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :", font=(FONT_NAME, 12, "normal"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password :", font=(FONT_NAME, 12, "normal"))
password_label.grid(column=0, row=3)

# Creating entry to accept input
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mihir@email.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Create buttons
generate_password_button = Button(text="Generate Password", bd=1, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, font=(FONT_NAME, 9, "normal"), bd=1, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
