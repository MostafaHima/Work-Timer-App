from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmark_label.config(text="♣")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_canvas, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        update_timer(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        update_timer(SHORT_BREAK_MIN * 60)

    else:
        timer_label.config(text="Work", fg=GREEN)
        update_timer(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def update_timer(count):
    minute = math.floor(count / 60)
    second = count % 60

    if second == 0 or second < 10:
        second = f"0{second}"

    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_canvas, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, update_timer, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=80, bg=YELLOW)

# --------------- Create Timer Text -----------------------------
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=1)
timer_label.config(bg=YELLOW)

# ------------------- Create photo Tomato -----------------------
canvas = Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
read_photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=read_photo)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)

# ----------------------- Create Buttons ----------------------------
button_start = Button(text="Start", fg="white", width=10, bg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", fg="white", width=10, bg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset)
button_reset.grid(column=2, row=3)

# ------------------------ Checkmarks -------------------------------------
checkmark_label = Label(text="♣", fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=4)
checkmark_label.config(background=YELLOW)

window.mainloop()
