from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# label
my_label = Label(text="I'm a Label.", font=("Comic Sans MS", 26, "bold"))
my_label.pack()
my_label["text"] = "New text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label["text"] = input_text.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input_text = Entry(width=20)
input_text.pack()


window.mainloop()
