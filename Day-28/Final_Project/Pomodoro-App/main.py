from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BROWN = "#564a4a"
FONT_NAME = "COMIC SANS MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg="darkseagreen4")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg="darkseagreen4")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_bg)
timer_text = canvas.create_text(105, 130, text="00:00", fill=BROWN, font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", bg="lemonchiffon2", command=start_timer)
start_button.grid(column=0, row=2)
start_button.config(padx=3, pady=3)

reset_button = Button(text="Reset", bg="lemonchiffon2", command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button.config(padx=3, pady=3)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg="darkseagreen4")
timer_label.grid(column=1, row=0)

# Checkmark
check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg="green4")
check_marks.grid(column=1, row=3)

window.mainloop()
