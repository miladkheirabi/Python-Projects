from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checkmarks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
    l1.config(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
    reps = 0
    checkmarks.clear()
    l2.config(text="".join(checkmarks))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, l1, l2
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        l2.config(text="")
        l1.config(text="Break", fg=RED, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        checkmarks.append(CHECK_MARK)
        l2.config(text="".join(checkmarks))
        l1.config(text="Break", fg=PINK, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
    else:
        count_down(WORK_SEC)
        l1.config(text="Work", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count > 0:
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
        else:
            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
checkmarks = []
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
l1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
l2 = Label(fg=GREEN, font=(FONT_NAME, 10), bg=YELLOW)
but1 = Button(text="Start", command=start_timer)
but2 = Button(text="Reset", command=reset_timer)
canvas.grid(row=1, column=1)
l1.grid(row=0, column=1)
but1.grid(row=2, column=0)
but2.grid(row=2, column=2)
l2.grid(row=3, column=1)

window.mainloop()
