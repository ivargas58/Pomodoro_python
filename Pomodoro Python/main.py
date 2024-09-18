from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#constante del tiempo a trabajar
WORK_MIN = 25
#constante del break corto
SHORT_BREAK_MIN = 5
#constante del break largo y final 
LONG_BREAK_MIN = 20
reps = 0 
timer =None

# ---------------------------- TIMER RESET ------------------------------- #
# Funcion ejecutada por el boton reset para reiniciar todo 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_label.config(text="")
    global reps 
    reps = 0
   
# ---------------------------- TIMER MECHANISM ------------------------------- #
#Funcion ejecutada por el boton star para comenzar el proceso de count
def start_timer():
    global reps
    reps += 1  
    #const
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    #Decicional para que en cada seccion se ejecute un tiempo en especifico y un titulo en especifico
    #Se ejecuta la seccion de break largo y final 
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    #Se ejecuta la seccion de break corto
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    #Se ejecuta la seccion de work 
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#Funcion que ejecuta counter y elimina segundo tras segundo 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    #Aqui decide si el counter esta 0 cero imprime un check mark de lo contario todo seguira su curso
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
#Window 
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Label
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

#Toda la seccion donde esta el tomate, el timer, los botones 
#Para mi canvas es como decir un container en css
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Boton de star
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
#Boton de reset
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
#Check label 
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


#sin esto no se ve la pantalla es como el exitonclick en turtle library
window.mainloop()
