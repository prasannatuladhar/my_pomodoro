from cgitb import text
from itertools import count
from math import floor
from tkinter import *
from playsound import playsound
from multiprocessing import Process

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = '#1D1D1D'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None

#---------------PLay Music---------------------#
def play_music():
    sound = value_inside.get()
    mysound = sound + "." + "mp3"
    playsound(mysound,block = False)

    

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_heading.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def call_timer():
    global reps
    reps =reps +1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN *60

    if reps %8==0:
        time_counter(long_break_sec)
        timer_heading.config(text="Break",fg=GREEN)
    elif reps%2==0:
        time_counter(short_break_sec) 
        timer_heading.config(text="Break",fg=GREEN)

    else:
        time_counter(work_sec)      
        timer_heading.config(text="Work",fg=RED)
        # check_label.config(text="✔")

        

       
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def time_counter(count):
    global timer,play_sound

    min_count = floor(count/60)
    sec_count = count%60
    if sec_count < 10:
        # sec_count="0" +str(sec_count)
        sec_count = f"0{sec_count}"
    
    canvas.itemconfig(timer_text,text=f"{min_count} : {sec_count}")
    if count >0:
        timer=window.after(1000,time_counter,count-1)
        
        

    else:
        call_timer()    
        marks= ""
        for _ in range(floor(reps/2)):
            marks +="✔"
        check_label.config(text=marks)    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
# window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width=500,height=625,highlightthickness=0)
img= PhotoImage(file = "bg_image.png")


canvas.create_image(250,314,image=img)
timer_heading = Label(text="TIMER",fg=GREEN,bg=BLACK,font=(FONT_NAME,30,"bold"))
# timer_heading.grid(column=2,row=2) 

timer_text = canvas.create_text(250,130,text="00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas.pack(expand=YES, fill=BOTH)

start_button = Button(text="Start",highlightthickness=0)
start_button.config(command=call_timer)
# start_button.grid(column=1,row=5)

play_sound = Button(text="Play ▶ ",font=(FONT_NAME,12,"bold"),highlightthickness=0,command=play_music)
# start_button.config(command=call_timer)

check_label = Label(fg=GREEN,bg=BLACK,font=(FONT_NAME,10,"bold"))
# check_label.grid(column=2,row=5)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
# reset_button.grid(column=3,row=5)

# Create the list of options
options_list = ["Nature Sound", "Jazz Music", "Ambient Music", "Deep Focus","Relaxing Music"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = StringVar(window)

# Set the default value of the variable
value_inside.set("Jazz Music")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
music_menu = OptionMenu(window, value_inside, *options_list)



    
# Display Buttons
timer_heading_canvas = canvas.create_window( 190, 50,
                                       anchor = "nw",
                                       window = timer_heading)  
start_button_canvas = canvas.create_window( 200, 160, 
                                       anchor = "nw",
                                       window = start_button)
play_sound_button_canvas = canvas.create_window( 260, 220, 
                                       anchor = "nw",
                                       window = play_sound)                                       
  
reset_button_canvas = canvas.create_window( 250, 160,
                                       anchor = "nw",
                                       window = reset_button)
  

check_label_canvas = canvas.create_window( 200, 190,
                                       anchor = "nw",
                                       window = check_label)
music_menu_canvas = canvas.create_window( 130, 220,
                                       anchor = "nw",
                                       window = music_menu)     


  
window.mainloop()
