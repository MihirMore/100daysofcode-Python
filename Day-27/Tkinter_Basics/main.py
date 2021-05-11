from tkinter import *


# Button
def button_clicked():
    my_label["text"] = input_text.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# label
my_label = Label(text="I'm a Label.", font=("Comic Sans MS", 26, "bold"))
my_label.pack()
my_label["text"] = "New text"
my_label.config(text="New Text")

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input_text = Entry(width=20)
input_text.insert(END, string="Type Something")
input_text.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio Button
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option1", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
