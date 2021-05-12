from tkinter import *


# Button
def button_clicked():
    my_label["text"] = input_text.get()


# Label
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=80)
# label
my_label = Label(text="I'm a Label.", font=("Comic Sans MS", 16, "bold"))
my_label.grid(column=0, row=0)

# Button
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input_text = Entry(width=20)
input_text.insert(END, string="Type Something")
input_text.grid(column=3, row=2)

window.mainloop()