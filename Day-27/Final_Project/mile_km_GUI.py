from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)


def miles_to_km():
    miles = entry_text.get()
    km = round(float(miles) * 1.609, 2)
    answer_label["text"] = km


# Label
is_equal_label = Label(text="is equal to", font=("Comic Sans MS", 10, "normal"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=30, pady=30)

# Entry
entry_text = Entry(width=15, bd=2, font=("default", 11))
entry_text.insert(END, string="0")
entry_text.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Comic Sans MS", 10, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=30, pady=30)

# Label
km_label = Label(text="Km", font=("Comic Sans MS", 10, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=30, pady=30)

# Label
answer_label = Label(text="0", font=("Comic Sans MS", 10, "normal"))
answer_label.grid(column=1, row=1)
answer_label.config(padx=30, pady=30)

# Button
convert_button = Button(text="Convert", command=miles_to_km)
convert_button.grid(column=1, row=2)

window.mainloop()
