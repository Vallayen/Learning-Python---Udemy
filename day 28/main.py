from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
X_MARK = "❌"
reps = 0
timer_type = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps, timer_type
  if reps == 0 or reps == 2 or reps == 4 or reps == 6:
    countdown(WORK_MIN*60)
    timer_type = "Work time"
    timer_label.config(text=timer_type)
    reps +=1
  elif reps == 1 or reps == 3 or reps == 5:
    countdown(SHORT_BREAK_MIN * 60)
    timer_type = "Short Break"
    timer_label.config(text=timer_type)
    reps +=1
  elif reps == 7:
    countdown(LONG_BREAK_MIN * 60)
    timer_label.config(text=timer_type)
    timer_type = "Long break"
    
    
def reset():
  global reps
  reps = 0
  canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec == 0:
    count_sec = "00"
  elif count_sec < 10 and count_sec > 0:
    count_sec = f"0{count_sec}"
  
  if count > 0:
    screen.after(1000, countdown, count - 1)
    
  else:
    start_timer()
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  timer_label.config(text=timer_type)
  
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.configure(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)


tomato = PhotoImage(file="tomato.png")

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.place(x=-25, y=175)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.place(x=190, y=175)

check = Label(fg=GREEN, text=CHECK_MARK, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check.place(x=85, y=230)

timer_label = Label(fg=GREEN, bg=YELLOW, text=timer_type, font=(FONT_NAME, 40, "bold"))
timer_label.place(x=-40, y=-45)

canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()



#Leave at bottom
screen.mainloop()
